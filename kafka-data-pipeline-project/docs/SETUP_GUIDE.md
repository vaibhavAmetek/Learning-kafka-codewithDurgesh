# 🚀 Complete Setup Guide (Step-by-Step)

> Beginner-friendly guide with detailed Hinglish explanations

---

## 📋 Prerequisites Check

### 1. Kafka Running Hai?
```bash
# Check karo
lsof -i :9092

# Agar nahi chal raha to start karo
cd /Users/vaibhavshukla/learningProjects/Learning-kafka-codewithDurgesh
./start-kafka.sh
```

### 2. Python Installed Hai?
```bash
# Version check karo
python3 --version

# Should be 3.8 or higher
```

---

## 🎯 Step-by-Step Setup

### Step 1: Project Folder Mein Jao
```bash
cd /Users/vaibhavshukla/learningProjects/Learning-kafka-codewithDurgesh/kafka-data-pipeline-project
```

### Step 2: Dependencies Install Karo
```bash
# Install all required libraries
pip3 install -r requirements.txt

# Ya ek ek karke:
pip3 install confluent-kafka
pip3 install faker
pip3 install requests
```

**Kya install ho raha hai?**
- `confluent-kafka` - Kafka Python client
- `faker` - Realistic fake data generate karne ke liye
- `requests` - HTTP calls ke liye (Druid integration)

### Step 3: Configuration Check Karo
```bash
# Config file dekho
cat config/kafka_config.py

# Verify karo:
# - bootstrap.servers = 'localhost:9092'
# - Topics defined hain
```

### Step 4: Test Run Karo

#### Terminal 1: Start Simple Producer
```bash
python3 producer/simple_producer.py
```

**Kya hoga?**
- Producer Kafka se connect hoga
- 5 test messages send karega
- Delivery confirmations dikhayega

#### Terminal 2: Start Simple Consumer
```bash
python3 consumer/simple_consumer.py
```

**Kya hoga?**
- Consumer Kafka se connect hoga
- Messages receive karega
- Console mein print karega

**Working? Congratulations! ✅**

---

## 📚 Task-wise Setup

### Task 1: Product Catalog

```bash
# Producer run karo
python3 producer/catalog_producer.py

# Choose option 3 (Quick test)
# 5 products send honge
```

### Task 2: Getting Started

```bash
# Already done in Step 4!
# simple_producer.py aur simple_consumer.py
```

### Task 3-7: Advanced Tasks

Detailed code files already created hain:
- All producers in `producer/` folder
- All consumers in `consumer/` folder
- Config in `config/` folder

---

## 🐛 Common Issues & Solutions

### Issue 1: Module Not Found
```bash
# Error: No module named 'confluent_kafka'
# Solution:
pip3 install confluent-kafka
```

### Issue 2: Connection Refused
```bash
# Error: Failed to connect to localhost:9092
# Solution: Start Kafka
cd ..
./start-kafka.sh
```

### Issue 3: Topic Not Found
```bash
# Don't worry! Topics auto-create hote hain
# Ya manually create karo:
cd ..
./create-topic.sh product-catalog
```

### Issue 4: Permission Denied
```bash
# Scripts executable nahi hain
chmod +x producer/*.py
chmod +x consumer/*.py
```

---

## ✅ Verification Checklist

- [ ] Kafka running on port 9092
- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip3 list | grep confluent`)
- [ ] simple_producer.py runs without errors
- [ ] simple_consumer.py receives messages
- [ ] catalog_producer.py sends products

---

## 🎓 Learning Order

### Day 1: Basics
1. Read `README.md`
2. Read `docs/TASKS.md`
3. Run `simple_producer.py`
4. Run `simple_consumer.py`
5. Understand the flow

### Day 2: Product Catalog
1. Read `catalog_producer.py` code
2. Run catalog producer
3. See products in consumer
4. Modify product templates
5. Add new categories

### Day 3: Advanced
1. Explore all producer files
2. Try different modes
3. Experiment with configurations
4. Build your own producer

---

## 📞 Need Help?

1. Check `docs/TROUBLESHOOTING.md`
2. Read code comments (detailed Hinglish)
3. Check `docs/TASKS.md` for task explanations
4. Review Kafka logs: `/opt/homebrew/var/log/kafka/`

---

**Setup complete? Start with Task 2 (simple_producer.py)! 🚀**
