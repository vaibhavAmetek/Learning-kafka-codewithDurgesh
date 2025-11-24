# 🐘 Install & Use Zookeeper with Kafka (Mac)

## Current Status

```
✅ Kafka 4.1.0: Installed
✅ KRaft Mode: Working (No Zookeeper)
❌ Zookeeper: Not installed
✅ broker.properties: Available
```

---

## 🎯 Two Ways to Use Zookeeper

### Option 1: Install Separate Zookeeper (Traditional)

- Install Zookeeper separately
- More control
- Can use for other projects too

### Option 2: Use Kafka's Built-in Zookeeper (Easier)

- Kafka comes with Zookeeper scripts
- No separate installation
- Just need config file

---

## 🚀 Method 1: Install Zookeeper via Homebrew

### Step 1: Install Zookeeper

```bash
brew install zookeeper
```

**Installation Output:**

```
==> Downloading zookeeper...
==> Installing zookeeper...
🍺  /opt/homebrew/Cellar/zookeeper/3.9.x: xxx files, xxMB
```

---

### Step 2: Create Zookeeper Config

```bash
# Create config file
cat > /opt/homebrew/etc/kafka/zookeeper.properties << 'EOF'
# Zookeeper Configuration
dataDir=/tmp/zookeeper
clientPort=2181
maxClientCnxns=0
admin.enableServer=false
tickTime=2000
initLimit=5
syncLimit=2
EOF
```

---

### Step 3: Start Zookeeper

**Terminal 1:**

```bash
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```

**Expected Output:**

```
[2024-11-22 19:20:00] INFO binding to port 0.0.0.0/0.0.0.0:2181
[2024-11-22 19:20:00] INFO Server environment:zookeeper.version=3.9.x
```

✅ **Zookeeper running on port 2181**

---

### Step 4: Start Kafka with Zookeeper

**Terminal 2:**

```bash
kafka-server-start /opt/homebrew/etc/kafka/broker.properties
```

**Expected Output:**

```
[2024-11-22 19:20:30] INFO [KafkaServer id=0] started (kafka.server.KafkaServer)
```

✅ **Kafka running on port 9092**

---

### Step 5: Test It!

**Terminal 3:**

```bash
# Create topic
kafka-topics --create --topic zookeeper-test --bootstrap-server localhost:9092

# Producer
kafka-console-producer --topic zookeeper-test --bootstrap-server localhost:9092
> Hello with Zookeeper!
> Working fine!

# Terminal 4: Consumer
kafka-console-consumer --topic zookeeper-test --from-beginning --bootstrap-server localhost:9092
Hello with Zookeeper!
Working fine!
```

---

## 🔧 Method 2: Use Kafka's Built-in Zookeeper Scripts

Kafka installation already has Zookeeper scripts! Just need config.

### Step 1: Check if Scripts Exist

```bash
ls -la /opt/homebrew/opt/kafka/bin/ | grep zookeeper
```

**If you see:**

```
zookeeper-server-start
zookeeper-server-stop
zookeeper-shell
```

✅ **Scripts available!**

---

### Step 2: Create Zookeeper Config (if not exists)

```bash
# Check if config exists
ls -la /opt/homebrew/etc/kafka/zookeeper.properties

# If not, create it:
cat > /opt/homebrew/etc/kafka/zookeeper.properties << 'EOF'
# Licensed to the Apache Software Foundation (ASF)
dataDir=/tmp/zookeeper
clientPort=2181
maxClientCnxns=0
admin.enableServer=false
tickTime=2000
initLimit=5
syncLimit=2
EOF
```

---

### Step 3: Start Using Kafka's Zookeeper

**Terminal 1:**

```bash
# Start Zookeeper (using Kafka's script)
/opt/homebrew/opt/kafka/bin/zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```

**Terminal 2:**

```bash
# Start Kafka
kafka-server-start /opt/homebrew/etc/kafka/broker.properties
```

---

## 📝 Complete Zookeeper Config File

```properties
# /opt/homebrew/etc/kafka/zookeeper.properties

# Data directory where Zookeeper stores data
dataDir=/tmp/zookeeper

# Port for client connections
clientPort=2181

# Maximum number of client connections (0 = unlimited)
maxClientCnxns=0

# Disable admin server (not needed for development)
admin.enableServer=false

# Time unit in milliseconds (heartbeat)
tickTime=2000

# Time for initial synchronization
initLimit=5

# Time for sending requests and getting acknowledgements
syncLimit=2

# Purge task interval (hours)
autopurge.purgeInterval=1

# Number of snapshots to retain
autopurge.snapRetainCount=3
```

---

## 📝 Update Broker Config for Zookeeper

Edit `/opt/homebrew/etc/kafka/broker.properties`:

```bash
nano /opt/homebrew/etc/kafka/broker.properties
```

**Add/Update these lines:**

```properties
# Broker ID
broker.id=0

# Listeners
listeners=PLAINTEXT://:9092

# Zookeeper connection string
zookeeper.connect=localhost:2181

# Zookeeper session timeout
zookeeper.session.timeout.ms=18000

# Log directory
log.dirs=/tmp/kafka-logs

# Number of partitions
num.partitions=3

# Replication factor
default.replication.factor=1

# Log retention hours
log.retention.hours=168
```

---

## 🎬 Complete Startup Script (Zookeeper Mode)

Create helper script:

```bash
cat > start-with-zookeeper.sh << 'EOF'
#!/bin/bash

echo "🐘 Starting Zookeeper..."
/opt/homebrew/opt/kafka/bin/zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties &
ZOOKEEPER_PID=$!

echo "⏳ Waiting for Zookeeper to start (5 seconds)..."
sleep 5

echo "🚀 Starting Kafka..."
kafka-server-start /opt/homebrew/etc/kafka/broker.properties &
KAFKA_PID=$!

echo ""
echo "✅ Started!"
echo "   Zookeeper PID: $ZOOKEEPER_PID (Port 2181)"
echo "   Kafka PID: $KAFKA_PID (Port 9092)"
echo ""
echo "To stop:"
echo "   kill $ZOOKEEPER_PID $KAFKA_PID"
echo ""
EOF

chmod +x start-with-zookeeper.sh
```

**Run it:**

```bash
./start-with-zookeeper.sh
```

---

## 🛑 Stop Script

```bash
cat > stop-zookeeper-kafka.sh << 'EOF'
#!/bin/bash

echo "🛑 Stopping Kafka..."
pkill -f kafka.Kafka

echo "🛑 Stopping Zookeeper..."
pkill -f zookeeper

echo "✅ Stopped!"
EOF

chmod +x stop-zookeeper-kafka.sh
```

**Run it:**

```bash
./stop-zookeeper-kafka.sh
```

---

## 🔍 Verify Zookeeper is Working

### Check Processes

```bash
# Check Zookeeper
lsof -i :2181

# Check Kafka
lsof -i :9092

# Check both
ps aux | grep -E "zookeeper|kafka"
```

---

### Test Zookeeper Connection

```bash
# Using telnet
telnet localhost 2181

# Type: stat
# Press Enter
# You'll see Zookeeper stats

# Or use Zookeeper shell
/opt/homebrew/opt/kafka/bin/zookeeper-shell localhost:2181

# Inside shell, type:
ls /
ls /brokers
ls /brokers/ids
```

---

### Check Kafka Logs

```bash
# Kafka should show Zookeeper connection
tail -f /opt/homebrew/var/log/kafka/server.log | grep -i zookeeper

# Should see:
# "Connecting to zookeeper on localhost:2181"
# "Connected to zookeeper"
```

---

## 🎯 Daily Workflow with Zookeeper

### Morning (Start Everything)

```bash
# Terminal 1: Start Zookeeper
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

# Wait 5 seconds

# Terminal 2: Start Kafka
kafka-server-start /opt/homebrew/etc/kafka/broker.properties

# Terminal 3: Work
kafka-topics --create --topic my-topic --bootstrap-server localhost:9092
```

---

### Evening (Stop Everything)

```bash
# Stop Kafka first (Terminal 2)
Ctrl+C

# Then stop Zookeeper (Terminal 1)
Ctrl+C

# Or use script
./stop-zookeeper-kafka.sh
```

---

## 🐛 Troubleshooting

### Issue 1: Zookeeper Won't Start

```bash
# Check if port 2181 is free
lsof -i :2181

# If occupied, kill it
kill -9 <PID>

# Clean Zookeeper data
rm -rf /tmp/zookeeper

# Restart
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```

---

### Issue 2: Kafka Can't Connect to Zookeeper

```bash
# 1. Check Zookeeper is running
lsof -i :2181

# 2. Check broker.properties has correct setting
cat /opt/homebrew/etc/kafka/broker.properties | grep zookeeper.connect
# Should show: zookeeper.connect=localhost:2181

# 3. Test Zookeeper connection
telnet localhost 2181
```

---

### Issue 3: Zookeeper Command Not Found

```bash
# Option A: Use full path
/opt/homebrew/opt/kafka/bin/zookeeper-server-start

# Option B: Install Zookeeper separately
brew install zookeeper

# Option C: Add to PATH
echo 'export PATH="/opt/homebrew/opt/kafka/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

## 📊 Comparison: Your Two Options

### Currently (KRaft Mode)

```bash
# Start (1 command)
kafka-server-start /opt/homebrew/etc/kafka/server.properties

Processes: 1
Memory: ~500MB
Ports: 9092, 9093
Startup: 5 seconds
```

### With Zookeeper

```bash
# Start (2 commands)
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
kafka-server-start /opt/homebrew/etc/kafka/broker.properties

Processes: 2
Memory: ~800MB
Ports: 2181, 9092
Startup: 10 seconds
```

---

## 💡 My Recommendation

### For Learning:

1. **Start with KRaft** (already working)
2. **Then try Zookeeper** (to understand difference)
3. **Compare both** (see pros/cons yourself)

### For Projects:

- **New projects**: Use KRaft
- **Legacy projects**: Use Zookeeper
- **Production**: Check company standard

---

## ✅ Quick Setup (Copy-Paste)

```bash
# 1. Create Zookeeper config
cat > /opt/homebrew/etc/kafka/zookeeper.properties << 'EOF'
dataDir=/tmp/zookeeper
clientPort=2181
maxClientCnxns=0
admin.enableServer=false
EOF

# 2. Start Zookeeper (Terminal 1)
/opt/homebrew/opt/kafka/bin/zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

# 3. Start Kafka (Terminal 2)
kafka-server-start /opt/homebrew/etc/kafka/broker.properties

# 4. Test (Terminal 3)
kafka-topics --create --topic test --bootstrap-server localhost:9092
kafka-console-producer --topic test --bootstrap-server localhost:9092
# Type: Hello Zookeeper!

# 5. Consume (Terminal 4)
kafka-console-consumer --topic test --from-beginning --bootstrap-server localhost:9092
```

---

## 🎓 Summary

**Question**: Can we run Zookeeper?
**Answer**: **Haan!**

**How:**

1. Kafka already has Zookeeper scripts
2. Just need to create `zookeeper.properties`
3. Start Zookeeper first, then Kafka
4. Everything else same

**Should you?**

- For learning: Try both modes
- For production: KRaft recommended
- For old tutorials: Zookeeper needed

**Try it now!** Follow "Quick Setup" above! 🚀
