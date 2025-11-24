# 🔥 Learning Apache Kafka (Hinglish Edition)

> Complete Apache Kafka learning resources with code examples, setup guides, and detailed notes in Hinglish (Hindi + English)

---

## 📚 What's Included

### 1. **Detailed Notes (Hinglish)**

- `Kafka_Notes_Part1_Basics.md` - Kafka concepts, architecture, real-world examples
- `Kafka_Topic_Partition_Detailed.md` - Deep dive into topics and partitions
- `Kafka_Console_Commands.md` - **NEW!** Complete console commands guide
- `kafka-mac-setup.md` - Complete setup guide for macOS

### 2. **Automated Installation Script**

- `install-kafka-mac.sh` - One-click Kafka installation for macOS

### 3. **iTerm2 Setup** ⭐ NEW!

- `ITERM_SETUP.md` - Complete iTerm2 configuration guide
- `setup-iterm-kafka.sh` - Auto-configure iTerm2 with transparency
- `kafka-iterm-layout.sh` - Create 4-pane Kafka development layout

### 4. **Helper Scripts** (Created by installation script)

- `start-kafka.sh` - Start Kafka server
- `stop-kafka.sh` - Stop Kafka server
- `create-topic.sh` - Create new topic
- `list-topics.sh` - List all topics
- `start-producer.sh` - Start producer console
- `start-consumer.sh` - Start consumer console

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Kafka

```bash
# Make script executable
chmod +x install-kafka-mac.sh

# Run installation
./install-kafka-mac.sh
```

**Script automatically karega:**

- ✅ Java 17+ install
- ✅ Homebrew check
- ✅ Kafka install
- ✅ Helper scripts create

### Step 2: Start Kafka

```bash
# Terminal 1: Start Kafka server
./start-kafka.sh
```

### Step 3: Create Topic

```bash
# Terminal 2: Create a topic
./create-topic.sh test-topic
```

### Step 4: Send Messages

```bash
# Terminal 2: Start producer
./start-producer.sh test-topic

# Type messages (press Enter after each):
> Hello Kafka!
> Learning Kafka is fun!
> This is my first message
```

### Step 5: Receive Messages

```bash
# Terminal 3: Start consumer
./start-consumer.sh test-topic

# You'll see all messages appear here!
```

---

## 📖 Learning Path

### 1. **Basics** (Start Here)

Read: `Kafka_Notes_Part1_Basics.md`

**You'll learn:**

- Kafka kya hai aur kyun chahiye
- Real-world examples (OLA, Zomato, Flipkart)
- Core concepts (Producer, Consumer, Broker, Topic)
- Architecture overview

### 2. **Topics & Partitions**

Read: `Kafka_Topic_Partition_Detailed.md`

**You'll learn:**

- Topic kya hai (Database table jaisa)
- Partition kya hai (Physical storage)
- Data kaise store hota hai
- Practical examples with diagrams

### 3. **Installation & Setup**

Read: `kafka-mac-setup.md`

**You'll learn:**

- Prerequisites
- Installation methods
- Configuration
- Kafka APIs
- Troubleshooting

---

## 📁 Project Structure

```
Learning-kafka-codewithDurgesh/
│
├── README.md                          # This file
├── Kafka_Notes_Part1_Basics.md        # Basic concepts (Hinglish)
├── Kafka_Topic_Partition_Detailed.md  # Topics & Partitions (Hinglish)
├── kafka-mac-setup.md                 # Setup guide (Hinglish)
│
├── install-kafka-mac.sh               # Automated installation script
│
└── [Created by script]:
    ├── start-kafka.sh                 # Start server
    ├── stop-kafka.sh                  # Stop server
    ├── create-topic.sh                # Create topic
    ├── list-topics.sh                 # List topics
    ├── start-producer.sh              # Producer console
    └── start-consumer.sh              # Consumer console
```

---

## 🎯 Key Concepts (Quick Reference)

### Apache Kafka Kya Hai?

```
Kafka = Distributed Event Streaming Platform

Think of it as:
  - Post Office (messages deliver karta hai)
  - Message Queue (messages store karta hai)
  - Data Pipeline (systems connect karta hai)
```

### Core Components:

```
┌─────────────┐      ┌──────────┐      ┌─────────────┐
│  PRODUCER   │─────>│  KAFKA   │─────>│  CONSUMER   │
│ (Sends data)│      │ (Stores) │      │(Reads data) │
└─────────────┘      └──────────┘      └─────────────┘
                           │
                      ┌────┴────┐
                      │ TOPICS  │
                      │ (P1,P2) │
                      └─────────┘
```

### Why Kafka?

```
✅ High Throughput: 1 lakh+ messages/second
✅ Scalable: Add brokers easily
✅ Durable: Data loss nahi hota
✅ Fault Tolerant: System crash se bachata hai
✅ Low Latency: Milliseconds mein data transfer
```

---

## 🛠️ Common Commands

### Topic Management

```bash
# Create topic
kafka-topics --create --topic my-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1

# List topics
kafka-topics --list --bootstrap-server localhost:9092

# Describe topic
kafka-topics --describe --topic my-topic --bootstrap-server localhost:9092

# Delete topic
kafka-topics --delete --topic my-topic --bootstrap-server localhost:9092
```

### Producer

```bash
# Console producer
kafka-console-producer --topic my-topic --bootstrap-server localhost:9092

# Producer with key
kafka-console-producer --topic my-topic \
  --bootstrap-server localhost:9092 \
  --property "parse.key=true" \
  --property "key.separator=:"
```

### Consumer

```bash
# Console consumer from beginning
kafka-console-consumer --topic my-topic \
  --from-beginning \
  --bootstrap-server localhost:9092

# Consumer with consumer group
kafka-console-consumer --topic my-topic \
  --bootstrap-server localhost:9092 \
  --group my-group

# Consumer with key
kafka-console-consumer --topic my-topic \
  --from-beginning \
  --bootstrap-server localhost:9092 \
  --property print.key=true \
  --property key.separator=":"
```

### Consumer Groups

```bash
# List consumer groups
kafka-consumer-groups --list --bootstrap-server localhost:9092

# Describe consumer group
kafka-consumer-groups --describe --group my-group --bootstrap-server localhost:9092

# Reset offset
kafka-consumer-groups --bootstrap-server localhost:9092 \
  --group my-group \
  --topic my-topic \
  --reset-offsets --to-earliest \
  --execute
```

---

## 🔥 Real-World Examples (From Notes)

### Example 1: OLA Driver Location Tracking

```
Problem: 10,000 drivers sending location every 3 seconds
         = 2 lakh updates per minute

Without Kafka: Database crash! 💥

With Kafka:
  Driver → Kafka Topic → Batch Consumer → Database
           (Buffer)      (100 at once)    (Smooth)

Result: No crash, real-time updates ✅
```

### Example 2: Zomato Food Tracking

```
Flow:
  Delivery Boy → Kafka → Multiple Consumers
                    |
        +-----------+-----------+-----------+
        |           |           |           |
    User App   Database   Analytics   Notifications

Benefits: One data source → Multiple uses
```

### Example 3: Flipkart Sale Notifications

```
Challenge: 10 crore users ko notification bhejni hai

Solution:
  Admin → Kafka → 100 Workers (Parallel)
           |
    Each worker: 10 lakh users

Result: All users notified in 2-3 minutes ✅
```

---

## 📊 Performance Tips

### 1. Partition Count

```bash
# Formula: Partitions = Throughput / Consumer Throughput
# Example: 100K msg/s ÷ 10K msg/s per consumer = 10 partitions
```

### 2. Replication Factor

```bash
# Production: replication-factor = 3 (recommended)
# Development: replication-factor = 1 (okay)
```

### 3. Batch Size

```bash
# Producer batch size (increase for throughput)
batch.size=16384  # Default
batch.size=32768  # Better for high throughput
```

### 4. Consumer Groups

```bash
# Max consumers in group = Number of partitions
# Example: 10 partitions → max 10 consumers in one group
```

---

## 🐛 Troubleshooting

### Issue 1: Port 9092 Already in Use

```bash
# Find process using port
lsof -i :9092

# Kill process
kill -9 <PID>
```

### Issue 2: Kafka Not Starting

```bash
# Check logs
tail -f /opt/homebrew/var/log/kafka/server.log

# Check Java version
java -version  # Should be 17+
```

### Issue 3: Topic Not Found

```bash
# List all topics
./list-topics.sh

# Create topic if missing
./create-topic.sh your-topic-name
```

### Issue 4: Consumer Not Receiving Messages

```bash
# Check if producer is connected
kafka-console-producer --topic test --bootstrap-server localhost:9092

# Check consumer from beginning
kafka-console-consumer --topic test --from-beginning --bootstrap-server localhost:9092
```

---

## 📚 Additional Resources

### Official Documentation

- Kafka Website: https://kafka.apache.org
- Quickstart: https://kafka.apache.org/quickstart
- Documentation: https://kafka.apache.org/documentation

### Community

- Kafka Summit: Main conference
- Local Meetups: Join Kafka meetup groups
- Stack Overflow: Tag `apache-kafka`

### Books

- "Kafka: The Definitive Guide" by Neha Narkhede
- "Kafka Streams in Action" by Bill Bejeck

---

## 🎓 Practice Projects

### Beginner Level

1. **Simple Chat Application**

   - Producer: Send messages
   - Consumer: Receive messages
   - Topic: chat-messages

2. **Log Aggregation**
   - Multiple services → Kafka
   - Centralized log consumer

### Intermediate Level

1. **E-commerce Order Processing**

   - Topics: orders, payments, shipments
   - Consumer groups for each service

2. **Real-time Analytics Dashboard**
   - Stream events to Kafka
   - Process with Kafka Streams
   - Display on dashboard

### Advanced Level

1. **Microservices Event Bus**

   - Multiple microservices
   - Event-driven architecture
   - CQRS pattern

2. **IoT Data Pipeline**
   - Millions of IoT devices
   - Real-time data processing
   - Kafka Streams + KSQL

---

## 🤝 Contributing

Feel free to:

- Report issues
- Suggest improvements
- Add more examples
- Translate to other languages

---

## 📝 License

This project is for educational purposes. Feel free to use and share!

---

## 👨‍💻 Author

**Learning Kafka with Durgesh**

- YouTube: Learn Code With Durgesh
- Instagram: @durgesh_k_t

---

## 🙏 Acknowledgments

- Apache Kafka community
- Learn Code With Durgesh tutorials
- All contributors and learners

---

## 📞 Support

Agar koi problem ho ya doubt ho:

1. Check troubleshooting section
2. Read detailed notes
3. Run `./list-topics.sh` to verify setup
4. Check Kafka logs: `/opt/homebrew/var/log/kafka/`

---

**Happy Learning! 🚀**

_Kafka seekhne ka maza lo aur real-world projects banao!_
