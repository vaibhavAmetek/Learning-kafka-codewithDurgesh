# 🐘 Zookeeper vs KRaft Mode (Mac)

## Quick Answer: Haan, Zookeeper Run Kar Sakte Ho!

Tumhare Mac pe **dono options available** hain:

1. **KRaft Mode** (Modern, Recommended) - No Zookeeper
2. **Zookeeper Mode** (Legacy, Old way) - With Zookeeper

---

## 🆚 Comparison

| Feature           | KRaft Mode            | Zookeeper Mode        |
| ----------------- | --------------------- | --------------------- |
| **Kafka Version** | 2.8+ (Stable in 3.0+) | All versions          |
| **Setup**         | Simpler (1 process)   | Complex (2 processes) |
| **Performance**   | Faster                | Slower                |
| **Maintenance**   | Easier                | More work             |
| **Production**    | Ready (Kafka 3.3+)    | Traditional           |
| **Learning**      | Modern approach       | Old approach          |

---

## 🎯 Your Options

### Option 1: KRaft Mode (Recommended - Already Setup)

**Pros:**

- ✅ Simpler (no Zookeeper needed)
- ✅ Faster startup
- ✅ Better performance
- ✅ Modern Kafka (future-proof)
- ✅ Less memory usage

**Cons:**

- ❌ Newer (less online tutorials use this)

**Commands:**

```bash
# One process only
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

---

### Option 2: Zookeeper Mode (Legacy)

**Pros:**

- ✅ More tutorials available
- ✅ Traditional approach
- ✅ Some old tools need it

**Cons:**

- ❌ Need to run 2 processes
- ❌ More complex setup
- ❌ Slower
- ❌ Being deprecated

**Commands:**

```bash
# Need 2 processes
# Terminal 1: Start Zookeeper
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

# Terminal 2: Start Kafka
kafka-server-start /opt/homebrew/etc/kafka/broker.properties
```

---

## 🚀 How to Run with Zookeeper (Your Mac)

### Step 1: Check Zookeeper Config Exists

```bash
ls -la /opt/homebrew/etc/kafka/zookeeper.properties
```

**If exists**, you're good to go!

---

### Step 2: Start Zookeeper First

**Terminal 1:**

```bash
# Start Zookeeper
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```

**Wait for:**

```
[2024-11-22 19:15:00] INFO binding to port 0.0.0.0/0.0.0.0:2181
```

✅ Zookeeper running on port **2181**

---

### Step 3: Start Kafka with Zookeeper Mode

**Terminal 2:**

```bash
# Start Kafka (broker mode)
kafka-server-start /opt/homebrew/etc/kafka/broker.properties
```

**Wait for:**

```
[2024-11-22 19:15:30] INFO [KafkaServer id=0] started
```

✅ Kafka running on port **9092**

---

### Step 4: Use Kafka (Same Commands)

**Terminal 3:**

```bash
# Create topic (same command)
kafka-topics --create --topic test --bootstrap-server localhost:9092

# Producer (same)
kafka-console-producer --topic test --bootstrap-server localhost:9092

# Consumer (same)
kafka-console-consumer --topic test --from-beginning --bootstrap-server localhost:9092
```

**Note**: Client commands **same hain** - Zookeeper backend mein kaam karta hai

---

## 📁 Config Files Comparison

### KRaft Mode (No Zookeeper)

```bash
/opt/homebrew/etc/kafka/server.properties
```

**Key Settings:**

```properties
# KRaft mode
process.roles=broker,controller
node.id=1
controller.quorum.voters=1@localhost:9093
listeners=PLAINTEXT://:9092,CONTROLLER://:9093
```

---

### Zookeeper Mode (Legacy)

**File 1: Zookeeper Config**

```bash
/opt/homebrew/etc/kafka/zookeeper.properties
```

**Settings:**

```properties
dataDir=/tmp/zookeeper
clientPort=2181
maxClientCnxns=0
```

**File 2: Kafka Broker Config**

```bash
/opt/homebrew/etc/kafka/broker.properties
```

**Settings:**

```properties
broker.id=0
listeners=PLAINTEXT://:9092
zookeeper.connect=localhost:2181
log.dirs=/tmp/kafka-logs
```

---

## 🔄 Complete Workflows

### Workflow 1: KRaft Mode (Modern)

```bash
# Terminal 1: One-time format
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties

# Start Kafka (single process)
kafka-server-start /opt/homebrew/etc/kafka/server.properties

# Terminal 2: Use Kafka
kafka-topics --create --topic test --bootstrap-server localhost:9092
```

**Processes Running:** 1 (Kafka only)

---

### Workflow 2: Zookeeper Mode (Legacy)

```bash
# Terminal 1: Start Zookeeper
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

# Terminal 2: Start Kafka
kafka-server-start /opt/homebrew/etc/kafka/broker.properties

# Terminal 3: Use Kafka
kafka-topics --create --topic test --bootstrap-server localhost:9092
```

**Processes Running:** 2 (Zookeeper + Kafka)

---

## 🎓 When to Use Which?

### Use KRaft Mode If:

- ✅ Learning Kafka (modern approach)
- ✅ New projects
- ✅ Want simplicity
- ✅ Performance matters
- ✅ Future-proof setup

### Use Zookeeper Mode If:

- ✅ Following old tutorials (pre-2022)
- ✅ Working with legacy systems
- ✅ Company uses old Kafka version
- ✅ Need compatibility with old tools

---

## 🛠️ Switching Between Modes

### Currently Using KRaft → Switch to Zookeeper

```bash
# 1. Stop Kafka (if running)
pkill -f kafka.Kafka

# 2. Clean KRaft data
rm -rf /tmp/kraft-combined-logs

# 3. Start Zookeeper
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

# 4. Start Kafka with broker config
kafka-server-start /opt/homebrew/etc/kafka/broker.properties
```

---

### Currently Using Zookeeper → Switch to KRaft

```bash
# 1. Stop Kafka and Zookeeper
pkill -f kafka.Kafka
pkill -f zookeeper

# 2. Clean old data
rm -rf /tmp/kafka-logs
rm -rf /tmp/zookeeper

# 3. Format for KRaft
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties

# 4. Start Kafka (KRaft mode)
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

---

## 🔍 How to Check Which Mode is Running

### Check Processes

```bash
# Check if Zookeeper running
lsof -i :2181

# Check if Kafka running
lsof -i :9092

# Check processes
ps aux | grep -E "zookeeper|kafka"
```

---

### Check Kafka Logs

```bash
# KRaft mode shows:
tail /opt/homebrew/var/log/kafka/server.log | grep -i kraft
# Output: "KRaft mode enabled"

# Zookeeper mode shows:
tail /opt/homebrew/var/log/kafka/server.log | grep -i zookeeper
# Output: "zookeeper.connect=localhost:2181"
```

---

## 📊 Resource Usage Comparison

### KRaft Mode

```
Memory: ~500MB
Processes: 1
Ports: 9092 (Kafka), 9093 (Controller)
Startup Time: ~5 seconds
```

### Zookeeper Mode

```
Memory: ~800MB (Zookeeper 300MB + Kafka 500MB)
Processes: 2
Ports: 2181 (Zookeeper), 9092 (Kafka)
Startup Time: ~10 seconds (Zookeeper first, then Kafka)
```

---

## 🐛 Troubleshooting Zookeeper Mode

### Issue 1: Zookeeper Won't Start

```bash
# Check port 2181
lsof -i :2181

# Clean Zookeeper data
rm -rf /tmp/zookeeper

# Restart
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```

---

### Issue 2: Kafka Can't Connect to Zookeeper

```bash
# Check Zookeeper is running
lsof -i :2181

# Check broker.properties
cat /opt/homebrew/etc/kafka/broker.properties | grep zookeeper.connect
# Should show: zookeeper.connect=localhost:2181

# Test connection
telnet localhost 2181
```

---

### Issue 3: Both Modes Conflicting

```bash
# Stop everything
pkill -f kafka
pkill -f zookeeper

# Clean all data
rm -rf /tmp/kafka-logs
rm -rf /tmp/zookeeper
rm -rf /tmp/kraft-combined-logs

# Choose one mode and start fresh
```

---

## 💡 Practical Example: Both Modes

### Example 1: KRaft Mode (Recommended)

```bash
# Terminal 1
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties
kafka-server-start /opt/homebrew/etc/kafka/server.properties

# Terminal 2
kafka-topics --create --topic orders --bootstrap-server localhost:9092
kafka-console-producer --topic orders --bootstrap-server localhost:9092
> order-1
> order-2

# Terminal 3
kafka-console-consumer --topic orders --from-beginning --bootstrap-server localhost:9092
order-1
order-2
```

**Total Terminals Needed:** 3 (1 for Kafka, 2 for work)

---

### Example 2: Zookeeper Mode

```bash
# Terminal 1: Zookeeper
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

# Terminal 2: Kafka
kafka-server-start /opt/homebrew/etc/kafka/broker.properties

# Terminal 3: Producer
kafka-topics --create --topic orders --bootstrap-server localhost:9092
kafka-console-producer --topic orders --bootstrap-server localhost:9092
> order-1
> order-2

# Terminal 4: Consumer
kafka-console-consumer --topic orders --from-beginning --bootstrap-server localhost:9092
order-1
order-2
```

**Total Terminals Needed:** 4 (1 for Zookeeper, 1 for Kafka, 2 for work)

---

## 📚 Learning Recommendation

### For Beginners (You):

```
Start with: KRaft Mode ✅
Reason:
- Simpler to understand
- Modern approach
- Less complexity
- Future of Kafka

Later learn: Zookeeper Mode
Reason:
- Understand legacy systems
- More tutorials use it
- Interview questions
```

### For Tutorials:

```
If tutorial says:
"Start Zookeeper first" → Old tutorial (pre-2022)
"Use KRaft mode" → New tutorial (2022+)

Both work! Just follow the tutorial's approach.
```

---

## 🎯 My Recommendation for You

**Use KRaft Mode** because:

1. ✅ **Simpler**: Ek hi process manage karna hai
2. ✅ **Modern**: Industry standard ban raha hai
3. ✅ **Faster**: Better performance
4. ✅ **Future-proof**: Zookeeper deprecated ho raha hai
5. ✅ **Already setup**: Tumhare system pe ready hai

**But learn Zookeeper** because:

- Many companies still use it
- Interview questions mein aata hai
- Old tutorials use it
- Good to know both

---

## 🔗 Quick Commands Reference

### KRaft Mode (No Zookeeper)

```bash
# Format (first time)
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties

# Start
kafka-server-start /opt/homebrew/etc/kafka/server.properties

# Stop
Ctrl+C or pkill -f kafka.Kafka
```

### Zookeeper Mode

```bash
# Start Zookeeper (Terminal 1)
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

# Start Kafka (Terminal 2)
kafka-server-start /opt/homebrew/etc/kafka/broker.properties

# Stop
Ctrl+C in both terminals
# Or
pkill -f zookeeper
pkill -f kafka.Kafka
```

---

## ✅ Summary

**Question**: Can we run Zookeeper?
**Answer**: **Haan!** Bilkul run kar sakte ho.

**But:**

- Kafka 4.1.0 mein **zarurat nahi** (KRaft mode better)
- Dono modes available hain tumhare Mac pe
- Client commands **same** rahenge
- KRaft **recommended** for new learning

**Try both** to understand the difference! 🚀

---

**Next**: Try KRaft first (simpler), then experiment with Zookeeper mode for learning! 📚
