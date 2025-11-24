# ⚡ Quick Start - Kafka on Mac (2 Minutes)

> **Your System**: macOS with Kafka 4.1.0 (Homebrew)
> **No Zookeeper Needed**: Uses KRaft mode

---

## 🎯 Super Quick (Copy-Paste Commands)

### Terminal 1: Start Kafka

```bash
# First time only - Format storage
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties

# Start Kafka
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

**Wait for**: `[KafkaServer id=1] started`

---

### Terminal 2: Create Topic & Send Messages

```bash
# Create topic
kafka-topics --create --topic quickstart --bootstrap-server localhost:9092

# Start producer
kafka-console-producer --topic quickstart --bootstrap-server localhost:9092
```

**Type messages:**

```
> Hello Mac!
> Kafka working!
> Press Ctrl+C to exit
```

---

### Terminal 3: Receive Messages

```bash
# Start consumer
kafka-console-consumer --topic quickstart --from-beginning --bootstrap-server localhost:9092
```

**You'll see:**

```
Hello Mac!
Kafka working!
Press Ctrl+C to exit
```

✅ **Working? Success!** 🎉

---

## 🔄 Daily Workflow

### Start Kafka (Every Time)

```bash
# Terminal 1
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

### Work with Topics

```bash
# Terminal 2
# Create
kafka-topics --create --topic my-topic --bootstrap-server localhost:9092

# List
kafka-topics --list --bootstrap-server localhost:9092

# Produce
kafka-console-producer --topic my-topic --bootstrap-server localhost:9092

# Terminal 3
# Consume
kafka-console-consumer --topic my-topic --from-beginning --bootstrap-server localhost:9092
```

### Stop Kafka

```bash
# In Terminal 1 where Kafka is running
Ctrl + C
```

---

## 🚀 Using Helper Scripts (Easier!)

### If you ran `install-kafka-mac.sh`:

```bash
# Start
./start-kafka.sh

# Create topic
./create-topic.sh my-topic

# Producer
./start-producer.sh my-topic

# Consumer (new terminal)
./start-consumer.sh my-topic

# List topics
./list-topics.sh

# Stop
./stop-kafka.sh
```

---

## 🐛 Quick Fixes

### Problem: Port 9092 in use

```bash
lsof -i :9092
kill -9 <PID>
```

### Problem: Kafka won't start

```bash
# Clean and restart
rm -rf /tmp/kraft-combined-logs
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

### Problem: Command not found

```bash
# Add to PATH
echo 'export PATH="/opt/homebrew/opt/kafka/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

## 📚 Next Steps

1. ✅ Kafka running? Read `MAC_COMMANDS.md` for all commands
2. ✅ Want theory? Read `Kafka_Notes_Part1_Basics.md`
3. ✅ Deep dive? Read `Kafka_Topic_Partition_Detailed.md`
4. ✅ Practice? Follow `QUICK_TEST.md`

---

## 💡 Key Differences from Windows

| Feature        | Windows                              | Mac (Your System)          |
| -------------- | ------------------------------------ | -------------------------- |
| Commands       | `.bat` files                         | Direct commands            |
| Zookeeper      | Needed (old Kafka)                   | **Not needed** (KRaft)     |
| Config path    | `C:\kafka\config\`                   | `/opt/homebrew/etc/kafka/` |
| Start command  | `bin\windows\kafka-server-start.bat` | `kafka-server-start`       |
| Path separator | `\`                                  | `/`                        |

---

**Your system is ready! Start with Terminal 1 commands above! 🚀**
