# 🎮 Kafka Console Commands - Complete Guide (Hinglish)

> **Prerequisite**: Kafka aur Zookeeper dono running hone chahiye

---

## 🚀 Let's Use Kafka with Console

Console se Kafka use karna bahut easy hai. Teen main steps hain:

```
1. Create new topic with kafka-topics
2. Produce example message with kafka-console-producer
3. Consume the message with kafka-console-consumer
```

---

## 📋 Prerequisites Check

### Verify Kafka & Zookeeper Running

```bash
# Check Zookeeper (Port 2181)
lsof -i :2181

# Check Kafka (Port 9092)
lsof -i :9092

# Both should show processes running
```

**Agar nahi chal rahe:**

```bash
# Terminal 1: Start Zookeeper
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

# Terminal 2: Start Kafka
kafka-server-start /opt/homebrew/etc/kafka/broker.properties
```

---

## 1️⃣ Create New Topic with kafka-topics

### Basic Topic Creation

```bash
kafka-topics --create \
  --topic my-first-topic \
  --bootstrap-server localhost:9092
```

**Output:**

```
Created topic my-first-topic.
```

---

### Topic with Custom Settings

```bash
kafka-topics --create \
  --topic orders-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

**Explanation:**

- `--topic orders-topic`: Topic ka naam
- `--partitions 3`: 3 partitions (parallel processing ke liye)
- `--replication-factor 1`: 1 copy (single broker setup ke liye)

---

### List All Topics

```bash
kafka-topics --list --bootstrap-server localhost:9092
```

**Output:**

```
my-first-topic
orders-topic
```

---

### Describe Topic (Details Dekho)

```bash
kafka-topics --describe \
  --topic orders-topic \
  --bootstrap-server localhost:9092
```

**Output:**

```
Topic: orders-topic
PartitionCount: 3
ReplicationFactor: 1
Configs:

Topic: orders-topic  Partition: 0  Leader: 0  Replicas: 0  Isr: 0
Topic: orders-topic  Partition: 1  Leader: 0  Replicas: 0  Isr: 0
Topic: orders-topic  Partition: 2  Leader: 0  Replicas: 0  Isr: 0
```

**Samjho:**

- **PartitionCount**: Kitne partitions hain
- **Leader**: Konsa broker handle kar raha hai
- **Replicas**: Kitni copies hain
- **Isr**: In-Sync Replicas (synchronized copies)

---

### Delete Topic

```bash
kafka-topics --delete \
  --topic my-first-topic \
  --bootstrap-server localhost:9092
```

**Output:**

```
Topic my-first-topic is marked for deletion.
```

---

## 2️⃣ Produce Example Message with kafka-console-producer

### Start Producer (Interactive Mode)

```bash
kafka-console-producer \
  --topic orders-topic \
  --bootstrap-server localhost:9092
```

**Prompt dikhega:**

```
>
```

**Ab messages type karo:**

```
> Order-1: Laptop purchased
> Order-2: Mobile purchased
> Order-3: Headphones purchased
```

**Har message ke baad Enter press karo.**

**Exit karne ke liye:** `Ctrl + C`

---

### Producer with Key (Key-Value Pairs)

```bash
kafka-console-producer \
  --topic orders-topic \
  --bootstrap-server localhost:9092 \
  --property "parse.key=true" \
  --property "key.separator=:"
```

**Format:** `key:value`

**Type karo:**

```
> user1:Order placed by user 1
> user2:Order placed by user 2
> user1:Another order by user 1
```

**Benefit:** Same key wale messages same partition mein jayenge (ordering guaranteed)

---

### Producer from File

```bash
# Create a file with messages
cat > messages.txt << EOF
Message 1: Hello Kafka
Message 2: Learning Kafka
Message 3: Console Producer
EOF

# Send file contents to Kafka
kafka-console-producer \
  --topic orders-topic \
  --bootstrap-server localhost:9092 < messages.txt
```

---

### Producer with Properties

```bash
kafka-console-producer \
  --topic orders-topic \
  --bootstrap-server localhost:9092 \
  --producer-property acks=all \
  --producer-property compression.type=snappy
```

**Properties:**

- `acks=all`: Wait for all replicas to acknowledge
- `compression.type=snappy`: Compress messages (save bandwidth)

---

## 3️⃣ Consume Messages with kafka-console-consumer

### Basic Consumer (From Beginning)

```bash
kafka-console-consumer \
  --topic orders-topic \
  --from-beginning \
  --bootstrap-server localhost:9092
```

**Output:**

```
Order-1: Laptop purchased
Order-2: Mobile purchased
Order-3: Headphones purchased
```

**Note:** `--from-beginning` se saare old messages bhi dikhenge

---

### Consumer (Only New Messages)

```bash
kafka-console-consumer \
  --topic orders-topic \
  --bootstrap-server localhost:9092
```

**Ye sirf naye messages show karega (jo ab aayenge)**

---

### Consumer with Key

```bash
kafka-console-consumer \
  --topic orders-topic \
  --from-beginning \
  --bootstrap-server localhost:9092 \
  --property print.key=true \
  --property key.separator=":"
```

**Output:**

```
user1:Order placed by user 1
user2:Order placed by user 2
user1:Another order by user 1
```

---

### Consumer with Consumer Group

```bash
kafka-console-consumer \
  --topic orders-topic \
  --bootstrap-server localhost:9092 \
  --group order-processors
```

**Benefits:**

- Multiple consumers ek group mein kaam kar sakte hain
- Load balancing automatic
- Offset tracking (resume from where left)

---

### Consumer with Offset Details

```bash
kafka-console-consumer \
  --topic orders-topic \
  --from-beginning \
  --bootstrap-server localhost:9092 \
  --property print.offset=true \
  --property print.partition=true \
  --property print.timestamp=true
```

**Output:**

```
Partition:0  Offset:0  Timestamp:1700645400000  Order-1: Laptop purchased
Partition:1  Offset:0  Timestamp:1700645401000  Order-2: Mobile purchased
Partition:2  Offset:0  Timestamp:1700645402000  Order-3: Headphones purchased
```

---

## 🎯 Complete Workflow Example

### Scenario: E-commerce Order Processing

**Step 1: Create Topic**

```bash
kafka-topics --create \
  --topic ecommerce-orders \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

---

**Step 2: Start Consumer (Terminal 1)**

```bash
kafka-console-consumer \
  --topic ecommerce-orders \
  --from-beginning \
  --bootstrap-server localhost:9092 \
  --property print.key=true \
  --property key.separator=":"
```

---

**Step 3: Produce Orders (Terminal 2)**

```bash
kafka-console-producer \
  --topic ecommerce-orders \
  --bootstrap-server localhost:9092 \
  --property "parse.key=true" \
  --property "key.separator=:"
```

**Type orders:**

```
> ORDER-001:{"product":"Laptop","price":50000,"user":"user1"}
> ORDER-002:{"product":"Mobile","price":20000,"user":"user2"}
> ORDER-003:{"product":"Headphones","price":2000,"user":"user1"}
```

---

**Step 4: Consumer Output (Terminal 1)**

```
ORDER-001:{"product":"Laptop","price":50000,"user":"user1"}
ORDER-002:{"product":"Mobile","price":20000,"user":"user2"}
ORDER-003:{"product":"Headphones","price":2000,"user":"user1"}
```

✅ **Real-time message flow working!**

---

## 🔥 Advanced Console Commands

### 1. Consumer Groups Management

**List all consumer groups:**

```bash
kafka-consumer-groups --list --bootstrap-server localhost:9092
```

**Describe consumer group:**

```bash
kafka-consumer-groups \
  --describe \
  --group order-processors \
  --bootstrap-server localhost:9092
```

**Output:**

```
GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
order-processors ecommerce-orders 0         10              10              0
order-processors ecommerce-orders 1         8               8               0
order-processors ecommerce-orders 2         12              12              0
```

**Explanation:**

- **CURRENT-OFFSET**: Consumer ne kitne messages read kiye
- **LOG-END-OFFSET**: Total messages in partition
- **LAG**: Kitne messages pending hain (0 = caught up)

---

### 2. Reset Consumer Offset

**Reset to earliest:**

```bash
kafka-consumer-groups \
  --bootstrap-server localhost:9092 \
  --group order-processors \
  --topic ecommerce-orders \
  --reset-offsets --to-earliest \
  --execute
```

**Reset to latest:**

```bash
kafka-consumer-groups \
  --bootstrap-server localhost:9092 \
  --group order-processors \
  --topic ecommerce-orders \
  --reset-offsets --to-latest \
  --execute
```

**Reset to specific offset:**

```bash
kafka-consumer-groups \
  --bootstrap-server localhost:9092 \
  --group order-processors \
  --topic ecommerce-orders:0 \
  --reset-offsets --to-offset 5 \
  --execute
```

---

### 3. Alter Topic Configuration

**Increase partitions:**

```bash
kafka-topics --alter \
  --topic ecommerce-orders \
  --partitions 5 \
  --bootstrap-server localhost:9092
```

**Change retention time:**

```bash
kafka-configs --alter \
  --entity-type topics \
  --entity-name ecommerce-orders \
  --add-config retention.ms=86400000 \
  --bootstrap-server localhost:9092
```

(86400000 ms = 24 hours)

---

### 4. Get Topic Offsets

```bash
kafka-run-class kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic ecommerce-orders
```

**Output:**

```
ecommerce-orders:0:10
ecommerce-orders:1:8
ecommerce-orders:2:12
```

---

## 🎨 Practical Examples

### Example 1: Chat Application

**Create chat topic:**

```bash
kafka-topics --create \
  --topic chat-messages \
  --bootstrap-server localhost:9092
```

**Terminal 1 (User 1 - Producer):**

```bash
kafka-console-producer \
  --topic chat-messages \
  --bootstrap-server localhost:9092
> User1: Hello everyone!
> User1: How are you?
```

**Terminal 2 (User 2 - Producer):**

```bash
kafka-console-producer \
  --topic chat-messages \
  --bootstrap-server localhost:9092
> User2: Hi User1!
> User2: I'm good, thanks!
```

**Terminal 3 (Chat Display - Consumer):**

```bash
kafka-console-consumer \
  --topic chat-messages \
  --from-beginning \
  --bootstrap-server localhost:9092
```

**Output:**

```
User1: Hello everyone!
User2: Hi User1!
User1: How are you?
User2: I'm good, thanks!
```

---

### Example 2: Log Aggregation

**Create logs topic:**

```bash
kafka-topics --create \
  --topic application-logs \
  --bootstrap-server localhost:9092 \
  --partitions 3
```

**Service A logs (Terminal 1):**

```bash
kafka-console-producer \
  --topic application-logs \
  --bootstrap-server localhost:9092
> [Service-A] INFO: Application started
> [Service-A] ERROR: Database connection failed
```

**Service B logs (Terminal 2):**

```bash
kafka-console-producer \
  --topic application-logs \
  --bootstrap-server localhost:9092
> [Service-B] INFO: API server running
> [Service-B] WARN: High memory usage
```

**Centralized log viewer (Terminal 3):**

```bash
kafka-console-consumer \
  --topic application-logs \
  --from-beginning \
  --bootstrap-server localhost:9092
```

---

### Example 3: Real-time Analytics

**Create events topic:**

```bash
kafka-topics --create \
  --topic user-events \
  --bootstrap-server localhost:9092 \
  --partitions 5
```

**Event producer:**

```bash
kafka-console-producer \
  --topic user-events \
  --bootstrap-server localhost:9092 \
  --property "parse.key=true" \
  --property "key.separator=:"
```

**Send events:**

```
> user123:{"event":"page_view","page":"/home"}
> user456:{"event":"click","button":"buy_now"}
> user123:{"event":"purchase","amount":5000}
```

**Analytics consumer:**

```bash
kafka-console-consumer \
  --topic user-events \
  --from-beginning \
  --bootstrap-server localhost:9092 \
  --property print.key=true \
  --property key.separator=":"
```

---

## 🐛 Common Issues & Solutions

### Issue 1: Topic Already Exists

**Error:**

```
Topic 'my-topic' already exists.
```

**Solution:**

```bash
# List topics to verify
kafka-topics --list --bootstrap-server localhost:9092

# Delete if needed
kafka-topics --delete --topic my-topic --bootstrap-server localhost:9092

# Or use different name
kafka-topics --create --topic my-topic-v2 --bootstrap-server localhost:9092
```

---

### Issue 2: Consumer Not Receiving Messages

**Problem:** Consumer running but no messages

**Solutions:**

1. **Check if producer sent messages:**

```bash
# Check topic has data
kafka-run-class kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic my-topic
```

2. **Use --from-beginning:**

```bash
kafka-console-consumer \
  --topic my-topic \
  --from-beginning \
  --bootstrap-server localhost:9092
```

3. **Check consumer group offset:**

```bash
kafka-consumer-groups \
  --describe \
  --group my-group \
  --bootstrap-server localhost:9092
```

---

### Issue 3: Connection Refused

**Error:**

```
Connection to node -1 could not be established
```

**Solution:**

```bash
# Check Kafka is running
lsof -i :9092

# If not running, start it
kafka-server-start /opt/homebrew/etc/kafka/broker.properties

# Check Zookeeper is running
lsof -i :2181
```

---

## 📊 Performance Tips

### 1. Batch Size for Producer

```bash
kafka-console-producer \
  --topic my-topic \
  --bootstrap-server localhost:9092 \
  --producer-property batch.size=32768 \
  --producer-property linger.ms=10
```

---

### 2. Consumer Fetch Size

```bash
kafka-console-consumer \
  --topic my-topic \
  --bootstrap-server localhost:9092 \
  --consumer-property fetch.min.bytes=1024 \
  --consumer-property fetch.max.wait.ms=500
```

---

### 3. Compression

```bash
kafka-console-producer \
  --topic my-topic \
  --bootstrap-server localhost:9092 \
  --producer-property compression.type=snappy
```

---

## 🎯 Quick Reference Card

```bash
# CREATE TOPIC
kafka-topics --create --topic <name> --bootstrap-server localhost:9092

# LIST TOPICS
kafka-topics --list --bootstrap-server localhost:9092

# DESCRIBE TOPIC
kafka-topics --describe --topic <name> --bootstrap-server localhost:9092

# DELETE TOPIC
kafka-topics --delete --topic <name> --bootstrap-server localhost:9092

# PRODUCER
kafka-console-producer --topic <name> --bootstrap-server localhost:9092

# CONSUMER
kafka-console-consumer --topic <name> --from-beginning --bootstrap-server localhost:9092

# CONSUMER GROUPS
kafka-consumer-groups --list --bootstrap-server localhost:9092
kafka-consumer-groups --describe --group <name> --bootstrap-server localhost:9092
```

---

## ✅ Practice Exercises

### Exercise 1: Basic Flow

```bash
# 1. Create topic
kafka-topics --create --topic practice-1 --bootstrap-server localhost:9092

# 2. Start consumer (Terminal 1)
kafka-console-consumer --topic practice-1 --from-beginning --bootstrap-server localhost:9092

# 3. Send messages (Terminal 2)
kafka-console-producer --topic practice-1 --bootstrap-server localhost:9092
> Message 1
> Message 2
> Message 3
```

---

### Exercise 2: Key-Value Messages

```bash
# Producer with keys
kafka-console-producer --topic practice-2 --bootstrap-server localhost:9092 \
  --property "parse.key=true" --property "key.separator=:"

# Consumer showing keys
kafka-console-consumer --topic practice-2 --from-beginning --bootstrap-server localhost:9092 \
  --property print.key=true --property key.separator=":"
```

---

### Exercise 3: Consumer Groups

```bash
# Start 2 consumers in same group
# Terminal 1
kafka-console-consumer --topic practice-3 --bootstrap-server localhost:9092 --group group-1

# Terminal 2
kafka-console-consumer --topic practice-3 --bootstrap-server localhost:9092 --group group-1

# Terminal 3: Send messages
kafka-console-producer --topic practice-3 --bootstrap-server localhost:9092

# Observe: Messages distributed between consumers!
```

---

## 🏆 Summary

**Three Main Commands:**

1. **kafka-topics**: Topic management
2. **kafka-console-producer**: Send messages
3. **kafka-console-consumer**: Receive messages

**Key Points:**

- ✅ Always use `--bootstrap-server localhost:9092`
- ✅ Use `--from-beginning` to see old messages
- ✅ Use keys for ordering within partition
- ✅ Use consumer groups for parallel processing
- ✅ Check offsets to track progress

**Next Steps:**

- Practice all examples
- Build mini projects
- Learn Kafka APIs (Java/Python)
- Explore Kafka Streams

---

**Happy Learning! Console commands master kar liye! 🎉**
