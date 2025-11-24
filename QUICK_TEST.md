# 🚀 Quick Kafka Test Guide (Hinglish)

Kafka install ho gaya? Ab test karo!

---

## 🎯 5-Minute Test (Step by Step)

### Step 1: Kafka Start Karo

Terminal 1 mein:

```bash
./start-kafka.sh
```

**Expected Output:**

```
Starting Apache Kafka...
[2024-11-22 10:45:00] INFO Kafka Server started
[2024-11-22 10:45:00] INFO Listening on port 9092
```

**Agar error aaye:**

- Check Java version: `java -version` (17+ chahiye)
- Check port 9092: `lsof -i :9092` (free hona chahiye)

---

### Step 2: Topic Create Karo

**Naya terminal** (Terminal 2) kholo:

```bash
./create-topic.sh first-test-topic
```

**Expected Output:**

```
Creating topic: first-test-topic
Created topic first-test-topic.
Topic created successfully!
```

**Verify karo:**

```bash
./list-topics.sh
```

**Output:**

```
Listing all Kafka topics...
first-test-topic
```

✅ Agar topic dikhe toh success!

---

### Step 3: Producer Start Karo (Messages Send)

Same terminal (Terminal 2) mein:

```bash
./start-producer.sh first-test-topic
```

**Expected:**

```
Starting Kafka Producer for topic: first-test-topic
Type your messages (Ctrl+C to exit):
>
```

**Ab messages type karo:**

```
> Hello Kafka!
> This is my first message
> Learning Kafka is awesome
> Producer working fine ✓
```

Har message ke baad **Enter** press karo.

💡 **Tip**: Messages immediately send ho jate hain (instant)

---

### Step 4: Consumer Start Karo (Messages Receive)

**Naya terminal** (Terminal 3) kholo:

```bash
./start-consumer.sh first-test-topic
```

**Expected Output:**

```
Starting Kafka Consumer for topic: first-test-topic
Hello Kafka!
This is my first message
Learning Kafka is awesome
Producer working fine ✓
```

✅ **Success**: Saare messages dikhe?

- Haan → Kafka working perfect! 🎉
- Nahi → Troubleshooting section dekho

---

### Step 5: Real-time Test

**Test karo real-time working:**

1. **Terminal 3** (Consumer) still running rakho
2. **Terminal 2** (Producer) mein naye messages type karo:

   ```
   > Real-time message 1
   > Real-time message 2
   > Instant delivery test
   ```

3. **Terminal 3** mein turant messages dikhne chahiye!

💡 **Magic**: Producer send kare → Consumer turant receive kare (milliseconds mein)

---

## 🔬 Advanced Tests

### Test 1: Multiple Consumers (Parallel Reading)

**Terminal 4** mein:

```bash
./start-consumer.sh first-test-topic
```

**Terminal 5** mein:

```bash
./start-consumer.sh first-test-topic
```

**Producer** (Terminal 2) se message bhejo:

```
> Message for multiple consumers
```

**Result**: Dono consumers ko message milega (broadcast)

---

### Test 2: Consumer Group Test

**Terminal 4** mein:

```bash
kafka-console-consumer --topic first-test-topic \
  --bootstrap-server localhost:9092 \
  --group group-1
```

**Terminal 5** mein:

```bash
kafka-console-consumer --topic first-test-topic \
  --bootstrap-server localhost:9092 \
  --group group-1
```

**Producer** se 4 messages bhejo:

```
> Message 1
> Message 2
> Message 3
> Message 4
```

**Result**: Messages distributed honge (load balancing):

- Consumer 1: Message 1, 3
- Consumer 2: Message 2, 4

---

### Test 3: Message Persistence

**Test karo ki messages store hain:**

1. **Stop all consumers** (Ctrl+C in each terminal)
2. **Producer** se naye messages bhejo:
   ```
   > Stored message 1
   > Stored message 2
   ```
3. **Stop producer** (Ctrl+C)
4. **Kafka bhi stop karo** (Terminal 1 mein Ctrl+C)
5. **Kafka restart karo**:
   ```bash
   ./start-kafka.sh
   ```
6. **Naya consumer start karo**:
   ```bash
   ./start-consumer.sh first-test-topic
   ```

**Result**: Saare old messages bhi dikhne chahiye! ✅

---

## 📊 Performance Test

### Test Message Throughput

**Producer** mein:

```bash
# 10,000 messages bhejo
for i in {1..10000}; do
  echo "Message $i" | kafka-console-producer \
    --topic first-test-topic \
    --bootstrap-server localhost:9092
done
```

**Consumer** mein:

```bash
# Count karo kitne messages received
kafka-console-consumer --topic first-test-topic \
  --from-beginning \
  --bootstrap-server localhost:9092 | wc -l
```

**Expected**: 10,000+ (including previous messages)

---

## 🎨 Fun Tests

### Test 1: JSON Messages

**Producer**:

```json
{"userId": 123, "action": "login", "timestamp": "2024-11-22T10:30:00"}
{"userId": 456, "action": "purchase", "amount": 999}
{"userId": 789, "action": "logout"}
```

**Consumer** show karega JSON as-is.

---

### Test 2: Emoji Messages 😄

**Producer**:

```
> Hello 👋
> Kafka is 🔥
> Learning is fun 🎉
```

**Consumer** mein emojis properly show honge!

---

### Test 3: Long Messages

**Producer** mein paste karo:

```
> This is a very long message to test Kafka's capability to handle large text. Apache Kafka is a distributed event streaming platform capable of handling trillions of events per day. It was originally developed by LinkedIn and later donated to the Apache Software Foundation.
```

**Result**: Complete message successfully receive hoga.

---

## ✅ Checklist (Sabhi Tests Pass Hone Chahiye)

```
□ Kafka successfully start ho raha hai
□ Topic create ho raha hai
□ Producer messages send kar raha hai
□ Consumer messages receive kar raha hai
□ Real-time messages instantly receive ho rahe hain
□ Multiple consumers ko messages mil rahe hain
□ Messages persistent hain (restart ke baad bhi available)
□ Consumer groups load balancing kar rahe hain
□ JSON aur emoji messages properly handle ho rahe hain
```

**Sab ✅ hain?** → Kafka perfectly configured hai! 🎉

---

## 🐛 Troubleshooting

### Problem 1: Producer Messages Send Nahi Ho Rahe

**Symptoms:**

- Messages type karte ho but consumer ko nahi mil rahe
- No error, but silent failure

**Solution:**

```bash
# Check if topic exists
./list-topics.sh

# Check Kafka is running
lsof -i :9092

# Check producer connection
kafka-console-producer --topic first-test-topic \
  --bootstrap-server localhost:9092 \
  --property "metadata.max.age.ms=1000"
```

---

### Problem 2: Consumer Messages Receive Nahi Kar Raha

**Symptoms:**

- Producer running but consumer blank screen

**Solution:**

```bash
# Check from beginning
kafka-console-consumer --topic first-test-topic \
  --from-beginning \
  --bootstrap-server localhost:9092

# Check topic has data
kafka-run-class kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic first-test-topic
```

---

### Problem 3: Kafka Start Nahi Ho Raha

**Symptoms:**

- Port 9092 already in use
- Java errors

**Solution:**

```bash
# Kill existing Kafka
pkill -f kafka

# Clear old logs
rm -rf /opt/homebrew/var/lib/kraft-combined-logs/*

# Restart
./start-kafka.sh
```

---

### Problem 4: Messages Duplicate Ho Rahe Hain

**Reason:** Multiple consumers without consumer group

**Solution:**

```bash
# Use consumer group
kafka-console-consumer --topic first-test-topic \
  --bootstrap-server localhost:9092 \
  --group my-app-group
```

---

## 📈 Next Steps

Sab tests pass ho gaye? Ab advanced topics try karo:

1. **Partitions with Keys**

   ```bash
   # Producer with key
   kafka-console-producer --topic test \
     --bootstrap-server localhost:9092 \
     --property "parse.key=true" \
     --property "key.separator=:"

   # Type: key:value
   user1:Hello from user 1
   user2:Hello from user 2
   ```

2. **Consumer Offsets**

   ```bash
   # Check consumer group offset
   kafka-consumer-groups --bootstrap-server localhost:9092 \
     --group my-group \
     --describe
   ```

3. **Multiple Topics**

   ```bash
   # Create multiple topics
   ./create-topic.sh topic-a
   ./create-topic.sh topic-b
   ./create-topic.sh topic-c

   # Consumer subscribe to multiple
   kafka-console-consumer \
     --bootstrap-server localhost:9092 \
     --whitelist "topic-.*"
   ```

---

## 🎓 Practice Exercises

### Exercise 1: Chat Application

```
Goal: Simple chat system banao

Steps:
1. Topic: "chat-room"
2. Terminal 1: User1 (producer)
3. Terminal 2: User2 (producer)
4. Terminal 3: Chat display (consumer)

Users message kare, display instantly dikhe!
```

### Exercise 2: Order Processing

```
Goal: Order pipeline banao

Topics:
- "orders" (new orders)
- "payments" (payment updates)
- "shipments" (shipping updates)

Test: Order place karo, track different stages
```

### Exercise 3: Log Aggregation

```
Goal: Multiple services ki logs ek jagah collect karo

Topics:
- "logs-service-a"
- "logs-service-b"
- "logs-service-c"

Consumer: All logs ek saath read kare
```

---

## 🏆 Final Challenge

**Build a complete pipeline:**

```
User Signup → Kafka → [Process] → Database
              |
              +----> [Send Email]
              +----> [Analytics]
              +----> [Notification]
```

**Topics:**

- user-signups
- email-queue
- analytics-events
- notifications

**Test:**

1. Producer signup event bheje
2. Multiple consumers parallel process karein
3. Each consumer apna kaam kare

**Success**: Ek event → Multiple actions (instantly!)

---

**All tests pass? Congratulations! 🎉**

Tum Kafka expert ban gaye ho! Ab real projects mein use karo.

**Happy Coding! 🚀**
