# 🔧 Troubleshooting Guide

> Common problems aur unke solutions (Hinglish)

---

## 🚨 Connection Issues

### Problem: Connection Refused (localhost:9092)
```
Error: Failed to connect to localhost:9092
```

**Causes:**
- Kafka running nahi hai
- Wrong port number
- Firewall blocking

**Solutions:**
```bash
# 1. Check if Kafka running hai
lsof -i :9092

# 2. Agar nahi chal raha, start karo
cd /Users/vaibhavshukla/learningProjects/Learning-kafka-codewithDurgesh
./start-kafka.sh

# 3. Wait karo 10-15 seconds
# 4. Phir se try karo
```

---

## 📦 Module/Import Issues

### Problem: No module named 'confluent_kafka'
```
ModuleNotFoundError: No module named 'confluent_kafka'
```

**Solution:**
```bash
# Install karo
pip3 install confluent-kafka

# Verify karo
pip3 list | grep confluent

# Should show: confluent-kafka 2.3.0
```

### Problem: No module named 'faker'
```
ModuleNotFoundError: No module named 'faker'
```

**Solution:**
```bash
# Install karo
pip3 install faker

# Ya saare dependencies ek saath
pip3 install -r requirements.txt
```

---

## 📝 Topic Issues

### Problem: Topic Not Found
```
Error: Topic 'product-catalog' not found
```

**Solution:**
```bash
# Don't worry! Auto-create hoga
# Ya manually create karo:
cd ..
./create-topic.sh product-catalog

# Verify karo
./list-topics.sh
```

### Problem: Messages Not Appearing
```
Consumer running hai but messages nahi dikh rahe
```

**Causes:**
- Producer aur consumer different topics use kar rahe hain
- Consumer late start hua aur 'latest' offset se padh raha hai
- Messages actually send nahi hue

**Solutions:**
```bash
# 1. Topic names check karo
# Producer: print(topic_name)
# Consumer: print(topic_name)

# 2. Consumer ko 'earliest' se start karo
# config/kafka_config.py mein check karo:
# 'auto.offset.reset': 'earliest'

# 3. Producer successfully send kar raha hai?
# Delivery callbacks check karo
```

---

## 🐍 Python Issues

### Problem: python: command not found
```
bash: python: command not found
```

**Solution:**
```bash
# Use python3 instead
python3 producer/simple_producer.py

# Ya alias banao
alias python=python3
```

### Problem: Permission Denied
```
Permission denied: './producer/simple_producer.py'
```

**Solution:**
```bash
# Executable banao
chmod +x producer/simple_producer.py

# Ya python se run karo
python3 producer/simple_producer.py
```

---

## ⚙️ Configuration Issues

### Problem: Wrong Bootstrap Server
```
Error: Failed to resolve 'localhost:9092'
```

**Solution:**
```bash
# config/kafka_config.py mein check karo
BOOTSTRAP_SERVERS = 'localhost:9092'

# Agar Kafka different port pe hai:
BOOTSTRAP_SERVERS = 'localhost:9093'  # Example
```

### Problem: Consumer Group Issues
```
Messages duplicate aa rahe hain ya nahi aa rahe
```

**Understanding:**
- Same group = Load balancing (messages divide)
- Different group = All get messages

**Solution:**
```bash
# config/kafka_config.py mein change karo
'group.id': 'your-unique-group-name'

# Ya code mein override karo:
config = get_consumer_config('my-custom-group')
```

---

## 💾 Data Issues

### Problem: JSON Decode Error
```
JSONDecodeError: Expecting value
```

**Causes:**
- Message JSON format mein nahi hai
- Corrupted data
- Wrong encoding

**Solution:**
```python
# Consumer mein try-except use karo
try:
    data = json.loads(message_value)
except json.JSONDecodeError:
    print(f"Invalid JSON: {message_value}")
    # Handle raw string
```

### Problem: Unicode/Encoding Errors
```
UnicodeDecodeError: 'utf-8' codec can't decode
```

**Solution:**
```python
# Proper encoding use karo
message_value = msg.value().decode('utf-8', errors='ignore')
```

---

## 🚀 Performance Issues

### Problem: Messages Slow Hai
```
Messages bahut slow send/receive ho rahe hain
```

**Solutions:**
```python
# 1. Batch size increase karo (producer)
'batch.size': 32768  # Default: 16384

# 2. Linger time add karo
'linger.ms': 10  # Wait 10ms for batching

# 3. Compression use karo
'compression.type': 'snappy'

# 4. More partitions
# Topic create karte waqt:
--partitions 5  # Instead of 3
```

### Problem: Consumer Lag
```
Consumer messages slowly process kar raha hai
```

**Solutions:**
```python
# 1. Poll timeout reduce karo
msg = consumer.poll(timeout=0.1)  # Instead of 1.0

# 2. Multiple consumers use karo (same group)
# Terminal 1: python consumer/simple_consumer.py
# Terminal 2: python consumer/simple_consumer.py

# 3. Batch processing karo
messages = []
for i in range(100):
    msg = consumer.poll(0.1)
    if msg:
        messages.append(msg)
# Process batch together
```

---

## 🔄 Kafka Server Issues

### Problem: Kafka Won't Start
```
Error starting Kafka server
```

**Solutions:**
```bash
# 1. Check logs
tail -100 /opt/homebrew/var/log/kafka/server.log

# 2. Port already in use?
lsof -i :9092
kill -9 <PID>

# 3. Clean data directory
rm -rf /tmp/kraft-combined-logs
# Then restart Kafka

# 4. Re-format storage
kafka-storage format -t $(kafka-storage random-uuid) \
  -c /opt/homebrew/etc/kafka/server.properties
```

### Problem: Kafka Crashes
```
Kafka suddenly stops
```

**Solutions:**
```bash
# 1. Check available disk space
df -h

# 2. Check memory
top

# 3. Check logs for errors
tail -200 /opt/homebrew/var/log/kafka/server.log

# 4. Restart Kafka
cd ..
./stop-kafka.sh
sleep 3
./start-kafka.sh
```

---

## 🧪 Testing Issues

### Problem: Can't Test End-to-End
```
Producer aur consumer dono test karna hai
```

**Solution:**
```bash
# Terminal 1: Start Kafka
./start-kafka.sh

# Terminal 2: Start Consumer (pehle!)
cd kafka-data-pipeline-project
python3 consumer/simple_consumer.py

# Terminal 3: Start Producer
cd kafka-data-pipeline-project
python3 producer/simple_producer.py

# Now watch messages flow!
```

---

## 📊 Debugging Tips

### Enable Detailed Logging
```python
# Producer/Consumer config mein add karo
'debug': 'broker,topic,msg'

# Ya specific debugging
'log_level': 0  # 0=DEBUG, 7=EMERG
```

### Print Everything
```python
# Har step pe print karo
print(f"Config: {config}")
print(f"Topic: {topic}")
print(f"Message: {message}")
print(f"Result: {result}")
```

### Use Try-Except Everywhere
```python
try:
    # Your code
    producer.send(message)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()  # Full error details
```

---

## 🆘 Still Stuck?

### Checklist:
- [ ] Kafka running? (`lsof -i :9092`)
- [ ] Dependencies installed? (`pip3 list`)
- [ ] Correct Python version? (`python3 --version`)
- [ ] Config file correct? (`cat config/kafka_config.py`)
- [ ] Logs checked? (`tail -f /opt/homebrew/var/log/kafka/server.log`)

### Get Help:
1. Read code comments (detailed explanations)
2. Check `docs/TASKS.md` for task details
3. Review `docs/SETUP_GUIDE.md` for setup steps
4. Check main project `README.md` and `INDEX.md`

---

**Most issues ka solution: Restart Kafka! 😄**

```bash
cd ..
./stop-kafka.sh
sleep 3
./start-kafka.sh
```
