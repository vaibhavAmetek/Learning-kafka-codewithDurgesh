# 🍎 Kafka Commands for Mac (Your System)

> Kafka version: **4.1.0** (Already installed via Homebrew)
> Location: `/opt/homebrew/opt/kafka`

---

## ✅ Current System Status

```bash
✅ Kafka installed: /opt/homebrew/opt/kafka
✅ Kafka version: 4.1.0
✅ Config location: /opt/homebrew/etc/kafka/
✅ Commands available: kafka-server-start, kafka-topics, etc.
```

---

## 🚀 Starting Kafka (Mac - No Zookeeper Needed!)

### Method 1: Using KRaft Mode (Recommended - Modern Kafka)

```bash
# Step 1: Generate Cluster UUID
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
echo $KAFKA_CLUSTER_ID

# Step 2: Format storage (ONLY FIRST TIME)
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties

# Step 3: Start Kafka Server
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

**Note**: Tumhare system pe **Zookeeper ki zarurat nahi** (Kafka 4.1.0 uses KRaft mode)

---

### Method 2: Using Homebrew Services (Background)

```bash
# Start Kafka as background service
brew services start kafka

# Check status
brew services list | grep kafka

# Stop service
brew services stop kafka

# Restart service
brew services restart kafka
```

---

## 📁 Important Paths (Your Mac)

```bash
# Kafka installation
/opt/homebrew/opt/kafka/

# Configuration files
/opt/homebrew/etc/kafka/
  ├── server.properties          # Main Kafka config
  ├── broker.properties          # Broker config
  ├── controller.properties      # Controller config
  ├── producer.properties        # Producer config
  └── consumer.properties        # Consumer config

# Kafka binaries (commands)
/opt/homebrew/opt/kafka/bin/
  ├── kafka-server-start
  ├── kafka-topics
  ├── kafka-console-producer
  ├── kafka-console-consumer
  └── ... (40+ commands)

# Data/Logs directory (default)
/tmp/kraft-combined-logs/

# Homebrew logs
/opt/homebrew/var/log/kafka/
```

---

## 🎯 Complete Workflow (Mac Specific)

### Step 1: Start Kafka

**Terminal 1:**

```bash
# One-time setup (if not done before)
# Generate unique cluster ID (UUID format)
# Cluster ID = Kafka cluster ka unique identifier
# Cluster = Multiple servers ka group jo ek saath kaam karte hain
# UUID = Universally Unique Identifier (random 128-bit number)
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
# Format storage directory with cluster ID
# Format = Initialize/prepare storage for first time use
# -t = cluster ID (unique identifier for this Kafka cluster)
# -c = config file path (server settings)
#
# CONFIG FILE KYUN ZAROORI HAI:
# 1. Centralized Settings: Sab settings ek jagah (port, memory, logs)
# 2. Reusability: Baar baar same settings use kar sakte hain
# 3. Environment Management: Dev/Prod alag configs rakh sakte hain
# 4. Easy Modification: Code change kiye bina settings badal sakte hain
# 5. Version Control: Git mein track kar sakte hain
#
# KAB HELPFUL HAI:
# - Multiple brokers setup (distributed system)
# - Different environments (development, staging, production)
# - Custom ports, memory limits, retention policies
# - Team collaboration (standardized settings)
#
# Ye command sirf PEHLI BAAR chalani hai, dubara nahi
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties

# Start Kafka server
# Ye command Kafka broker ko start karti hai
#
# CLUSTER ID SE RELATION:
# - Broker start hote waqt /tmp/kraft-combined-logs/ directory check karega
# - Waha stored meta.properties file mein cluster.id verify karega
# - Agar cluster.id match nahi hua toh error dega:
#   "INCONSISTENT_CLUSTER_ID: The Cluster ID doesn't match stored clusterId"
#
# ERROR KE BAAD KYA HOGA:
# 1. Broker start nahi hoga (startup fail)
# 2. Console mein error message dikhega
# 3. Process terminate ho jayega
#
# FIX KAISE KAREIN:
# Option 1: Purani logs delete karo
#   rm -rf /tmp/kraft-combined-logs
#   Phir format command dubara chalao (naya cluster ID ke saath)
#
# Option 2: Same cluster ID use karo jo pehle format mein use kiya tha
#   meta.properties file mein dekho: cluster.id=xyz
#   Wahi ID use karke format karo
#
# PRODUCTION MEIN:
# - Cluster ID hamesha same rakhni chahiye (consistency ke liye)
# - Backup lena zaroori hai (data loss se bachne ke liye)
#
# Server port 9092 par listen karega (default)
# Ctrl+C se stop hoga
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

**Wait for this message:**

```
[KafkaServer id=1] started (kafka.server.KafkaServer)
```

---

### Step 2: Create Topic

**Terminal 2:**

```bash
# Create topic with 3 partitions
# kafka-topics = Topic management command
# --create = Naya topic banao
# --topic = Topic ka naam (my-first-topic)
# --bootstrap-server = Kafka server ka address (localhost:9092)
# --partitions 3 = 3 partitions banao (data ko 3 parts mein divide karega)
# --replication-factor 1 = 1 copy rakhega (backup ke liye, single broker mein 1 hi rakh sakte hain)
kafka-topics --create \
  --topic my-first-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1

# List all topics
# Sab topics ke naam dikhao
kafka-topics --list --bootstrap-server localhost:9092

# Describe topic
# Topic ki detailed info dikhao (partitions, replicas, leader)
kafka-topics --describe --topic my-first-topic --bootstrap-server localhost:9092
```

**Expected Output:**

```
Created topic my-first-topic.
```

---

### Step 3: Start Producer (Send Messages)

**Terminal 2:**

```bash
# Producer start karo (message bhejne ke liye)
# --topic = Kis topic par message bhejenge
# --bootstrap-server = Kafka server ka address
# Ye command interactive mode mein khulega (> prompt dikhega)
kafka-console-producer --topic my-first-topic --bootstrap-server localhost:9092
```

**Type messages:**

```
> Hello from Mac!
> Kafka 4.1.0 working
> This is awesome
```

Press `Ctrl+C` to exit.

---

### Step 4: Start Consumer (Receive Messages)

**Terminal 3:**

```bash
# Consumer start karo (message receive karne ke liye)
# --topic = Kis topic se message read karenge
# --from-beginning = Pehle se stored sab messages dikha do
# --bootstrap-server = Kafka server ka address
kafka-console-consumer \
  --topic my-first-topic \
  --from-beginning \
  --bootstrap-server localhost:9092
```

**Output:**

```
Hello from Mac!
Kafka 4.1.0 working
This is awesome
```

---

## 🛠️ Common Commands (Mac)

### Topic Management

```bash
# Create topic
# Topic = Ek folder jaise, jisme messages store hote hain
# Partitions = Data ko kitne parts mein divide karna hai (parallel processing ke liye)
# Replication factor = Kitni copies rakhni hain (backup ke liye)
kafka-topics --create --topic test-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1

# List topics
# Sare topics ke naam dikhao
kafka-topics --list --bootstrap-server localhost:9092

# Describe topic
# Topic ki puri details dikhao:
# - Kitne partitions hain
# - Har partition ka leader kaun hai
# - Replicas kahan hain
kafka-topics --describe --topic test-topic --bootstrap-server localhost:9092

# Delete topic
# Topic ko permanently delete kar do (sab data delete ho jayega)
kafka-topics --delete --topic test-topic --bootstrap-server localhost:9092

# Alter topic (increase partitions)
# Existing topic mein partitions badhao (3 se 5 kar do)
# Note: Partitions sirf badha sakte hain, kam nahi kar sakte
kafka-topics --alter --topic test-topic \
  --partitions 5 \
  --bootstrap-server localhost:9092
```

---

### Producer Commands

```bash
# Simple producer
# Seedha messages type karo aur Enter press karo
# Har line ek separate message ban jayegi
kafka-console-producer --topic test-topic --bootstrap-server localhost:9092

# Producer with key
# Key-value pair bhejo (key:value format)
# parse.key=true = Key ko parse karo
# key.separator=":" = Key aur value ko ":" se separate karo
# Use case: Same key wale messages same partition mein jayenge
kafka-console-producer --topic test-topic \
  --bootstrap-server localhost:9092 \
  --property "parse.key=true" \
  --property "key.separator=:"

# Type: key:value
# Format: key:value (colon se separate)
user1:Hello from user 1
user2:Hello from user 2
```

---

### Consumer Commands

```bash
# Consumer from beginning
# Topic ke pehle message se lekar latest tak sab dikha do
# --from-beginning = Start from first message
kafka-console-consumer --topic test-topic \
  --from-beginning \
  --bootstrap-server localhost:9092

# Consumer with consumer group
# Consumer group = Multiple consumers ek group mein (load balancing ke liye)
# Ek group ke sab consumers milkar messages process karte hain
# --group = Consumer group ka naam
kafka-console-consumer --topic test-topic \
  --bootstrap-server localhost:9092 \
  --group my-consumer-group

# Consumer with key
# Key aur value dono dikha do
# print.key=true = Key ko print karo
# key.separator=":" = Key aur value ke beech ":" dikha do
kafka-console-consumer --topic test-topic \
  --from-beginning \
  --bootstrap-server localhost:9092 \
  --property print.key=true \
  --property key.separator=":"

# Consumer from specific offset
# Specific position se read karo
# --partition 0 = Partition 0 se read karo
# --offset 10 = 10th message se start karo (0-9 skip ho jayenge)
# Offset = Message ka position number (0 se start hota hai)
kafka-console-consumer --topic test-topic \
  --bootstrap-server localhost:9092 \
  --partition 0 \
  --offset 10
```

---

### Consumer Group Commands

```bash
# List all consumer groups
# Sare consumer groups ke naam dikhao
kafka-consumer-groups --list --bootstrap-server localhost:9092

# Describe consumer group
# Consumer group ki detailed info:
# - Kitne consumers hain
# - Har consumer kaunse partitions read kar raha hai
# - Current offset (kahan tak read kiya)
# - Lag (kitne messages pending hain)
kafka-consumer-groups --describe \
  --group my-consumer-group \
  --bootstrap-server localhost:9092

# Reset offset to earliest
# Consumer group ka offset reset kar do (pehle message par)
# --reset-offsets = Offset reset karo
# --to-earliest = Sabse pehle message par set karo
# --execute = Actually reset kar do (dry-run nahi)
# Use case: Sare messages dubara read karne hain
kafka-consumer-groups --bootstrap-server localhost:9092 \
  --group my-consumer-group \
  --topic test-topic \
  --reset-offsets --to-earliest \
  --execute

# Reset offset to latest
# Consumer group ka offset latest message par set karo
# --to-latest = Latest message par set karo
# Use case: Purane messages skip kar ke latest se start karna hai
kafka-consumer-groups --bootstrap-server localhost:9092 \
  --group my-consumer-group \
  --topic test-topic \
  --reset-offsets --to-latest \
  --execute

# Delete consumer group
# Consumer group ko delete kar do
# Note: Sirf tab delete hoga jab koi consumer active na ho
kafka-consumer-groups --bootstrap-server localhost:9092 \
  --group my-consumer-group \
  --delete
```

---

## 🔍 Monitoring & Debugging

### Check Kafka Status

```bash
# Check if Kafka is running
# Check if port 9092 is in use (Kafka ka default port)
# lsof = List Open Files
# -i :9092 = Internet connections on port 9092
# Output: Process ka naam, PID, user jo port use kar raha hai
lsof -i :9092

# Check Kafka process details
# ps = Process Status (running processes dikhata hai)
# aux = a(all users), u(user format), x(background processes)
# grep kafka = Sirf Kafka related lines filter karo
# Output: Kafka process running hai ya nahi, PID, memory usage
ps aux | grep kafka

# Check Homebrew service status
# brew services = Homebrew ke background services manage karta hai
# list = Sab services dikhao (running/stopped)
# grep kafka = Sirf Kafka ki line dikhao
# Output: Service name, status (started/stopped), user
brew services list | grep kafka
```

---

### View Logs

# Real-time logs (live updates dekhne ke liye)

# tail -f = Follow mode (jaise WhatsApp mein messages aate rehte hain)

# Kafka ke logs continuously screen par dikhate rahega

# Ctrl+C se exit karo

tail -f /opt/homebrew/var/log/kafka/server.log

# Last 100 lines (pichli 100 log entries)

# tail -100 = Sirf last 100 lines dikhao

# Jaise phone ki call history mein last 100 calls

# Kafka ne kya kiya recent mein, wo dikhega

tail -100 /opt/homebrew/var/log/kafka/server.log

# Search for errors (sirf galtiyan dhundho)

# grep ERROR = Sirf wo lines dikhao jisme "ERROR" word hai

# Jaise Ctrl+F karke "ERROR" search karna

# Agar Kafka mein koi problem hai toh yaha dikhega

# Output: ERROR wali lines with timestamp and details

grep ERROR /opt/homebrew/var/log/kafka/server.log

---

### Check Topic Data

```bash
# Get topic offsets (Har partition ka latest offset number dekho)
# kafka-run-class = Kafka ka internal Java class run karta hai
# GetOffsetShell = Tool jo offset information deta hai
# Offset = Message ka unique ID/number (0 se start hota hai)
# --broker-list = Kafka server ka address (localhost:9092)
# --topic = Kis topic ka offset dekhna hai
# Output: test-topic:0:150 (partition 0 mein 150 messages hain)
# Use case: Kitne messages produce hue, wo count karna
kafka-run-class kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic test-topic

# Dump log segments (Partition ki file ka andar ka data dekho)
# kafka-dump-log = Log file ka content read karta hai
# --files = Kis file ko read karna hai (full path chahiye)
# /tmp/kraft-combined-logs/ = Kafka ka default data directory
# test-topic-0 = Topic name + Partition number
# 00000000000000000000.log = Actual message file (segment)
# --print-data-log = Messages ka actual content print karo
# Output: Offset, timestamp, key, value, headers sab dikhega
# Use case: Debugging - kya data store hua hai wo dekhna
kafka-dump-log --files /tmp/kraft-combined-logs/test-topic-0/00000000000000000000.log \
  --print-data-log
```

---

## 🛑 Stopping Kafka

### Method 1: Stop Server (Terminal)

```bash
# In the terminal where Kafka is running
Ctrl + C
```

---

### Method 2: Stop Service (Homebrew)

```bash
brew services stop kafka
```

---

### Method 3: Kill Process

```bash
# Find Kafka process
ps aux | grep kafka

# Kill process
pkill -f kafka.Kafka

# Or force kill
pkill -9 -f kafka.Kafka
```

---

## 🧹 Clean Up Data

```bash
# Remove Kafka data (CAUTION: Deletes all topics/messages)
rm -rf /tmp/kraft-combined-logs

# Remove Homebrew logs
rm -rf /opt/homebrew/var/log/kafka/*

# After cleanup, format storage again before starting
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties
```

---

## ⚙️ Configuration (Mac Specific)

### Edit Kafka Config

```bash
# Open server.properties
nano /opt/homebrew/etc/kafka/server.properties

# Or use VS Code
code /opt/homebrew/etc/kafka/server.properties
```

### Important Settings

```properties
# Server ID
node.id=1

# Listeners
listeners=PLAINTEXT://localhost:9092

# Log directory
log.dirs=/tmp/kraft-combined-logs

# Number of partitions (default)
num.partitions=3

# Replication factor
default.replication.factor=1

# Log retention (7 days)
log.retention.hours=168

# Log segment size (1GB)
log.segment.bytes=1073741824
```

---

## 🐛 Troubleshooting (Mac)

### Issue 1: Port 9092 Already in Use

```bash
# Find process using port
lsof -i :9092

# Kill process (replace PID)
kill -9 <PID>

# Or kill all Kafka processes
pkill -f kafka.Kafka
```

---

### Issue 2: Kafka Won't Start

```bash
# Check Java version (need 17+)
java -version

# Check logs for errors
tail -50 /opt/homebrew/var/log/kafka/server.log

# Try formatting storage again
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties
```

---

### Issue 3: Command Not Found

```bash
# Add Kafka to PATH
echo 'export PATH="/opt/homebrew/opt/kafka/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Verify
which kafka-topics
```

---

### Issue 4: Permission Denied

```bash
# Fix permissions
sudo chown -R $(whoami) /opt/homebrew/var/lib/kafka-logs
sudo chown -R $(whoami) /tmp/kraft-combined-logs
```

---

## 📊 Performance Tuning (Mac)

### Increase Memory for Kafka

```bash
# Edit environment variables
export KAFKA_HEAP_OPTS="-Xmx2G -Xms2G"

# Then start Kafka
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

---

### Optimize for Development

```bash
# Edit server.properties
nano /opt/homebrew/etc/kafka/server.properties

# Add/modify:
num.network.threads=4
num.io.threads=8
socket.send.buffer.bytes=102400
socket.receive.buffer.bytes=102400
socket.request.max.bytes=104857600
```

---

## 🎯 Quick Reference Card

```bash
# START
kafka-server-start /opt/homebrew/etc/kafka/server.properties

# CREATE TOPIC
kafka-topics --create --topic test --bootstrap-server localhost:9092

# PRODUCER
kafka-console-producer --topic test --bootstrap-server localhost:9092

# CONSUMER
kafka-console-consumer --topic test --from-beginning --bootstrap-server localhost:9092

# LIST TOPICS
kafka-topics --list --bootstrap-server localhost:9092

# STOP
Ctrl+C or brew services stop kafka
```

---

## 🔗 Comparison: Windows vs Mac

| Task            | Windows Command                                                      | Mac Command                                                    |
| --------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| Start Kafka     | `bin\windows\kafka-server-start.bat config\server.properties`        | `kafka-server-start /opt/homebrew/etc/kafka/server.properties` |
| Start Zookeeper | `bin\windows\zookeeper-server-start.bat config\zookeeper.properties` | **Not needed** (KRaft mode)                                    |
| Config Path     | `C:\kafka\config\`                                                   | `/opt/homebrew/etc/kafka/`                                     |
| Binaries        | `bin\windows\*.bat`                                                  | `/opt/homebrew/opt/kafka/bin/*` (no .bat)                      |
| Path Separator  | `\` (backslash)                                                      | `/` (forward slash)                                            |

---

## 💡 Pro Tips for Mac

1. **Use Homebrew Services**

   ```bash
   brew services start kafka  # Background service
   ```

2. **Create Aliases** (Add to `~/.zshrc`)

   ```bash
   alias kstart='kafka-server-start /opt/homebrew/etc/kafka/server.properties'
   alias kcreate='kafka-topics --create --bootstrap-server localhost:9092 --topic'
   alias klist='kafka-topics --list --bootstrap-server localhost:9092'
   alias kproduce='kafka-console-producer --bootstrap-server localhost:9092 --topic'
   alias kconsume='kafka-console-consumer --bootstrap-server localhost:9092 --from-beginning --topic'
   ```

3. **Use iTerm2** for multiple terminals (better than default Terminal)

4. **Monitor with Activity Monitor**
   ```bash
   # Open Activity Monitor and search for "kafka"
   ```

---

## ✅ Verification Checklist

```bash
# 1. Check Kafka installed
brew list kafka

# 2. Check commands available
which kafka-topics

# 3. Check config exists
ls -la /opt/homebrew/etc/kafka/

# 4. Test start (format first time)
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties
kafka-server-start /opt/homebrew/etc/kafka/server.properties

# 5. In new terminal, test topic
kafka-topics --create --topic test --bootstrap-server localhost:9092
kafka-topics --list --bootstrap-server localhost:9092
```

---

**All commands tested on macOS with Kafka 4.1.0 (Homebrew installation) ✅**

**No Zookeeper needed - KRaft mode by default! 🚀**
