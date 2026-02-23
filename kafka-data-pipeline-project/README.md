# 🚀 Kafka Data Pipeline Project

> **Python → Confluent Kafka → Druid → Grafana**  
> Complete beginner-friendly data pipeline with Hinglish comments

---

## 📊 Project Architecture

```
Python Script (Producer)
    ↓
Confluent Kafka (Message Broker)
    ↓
Druid (Data Storage & Analytics)
    ↓
Grafana (Visualization Dashboard)
```

---

## 🎯 What This Project Does

**Real-world Example:** Imagine Zomato tracking food deliveries

1. **Python Script** - Delivery boy ka location aur order status generate karta hai
2. **Kafka** - Ye data real-time mein store karta hai (buffer ki tarah)
3. **Druid** - Historical data store karta hai aur fast queries run karta hai
4. **Grafana** - Beautiful dashboards mein data visualize karta hai

---

## 📁 Project Structure

```
kafka-data-pipeline-project/
│
├── README.md                    # Ye file (project guide)
├── requirements.txt             # Python dependencies
├── setup.sh                     # One-click setup script
│
├── producer/                    # Data generate karne wale scripts
│   ├── simple_producer.py       # Basic producer (Task 2)
│   ├── catalog_producer.py      # Product catalog producer (Task 1)
│   └── streaming_producer.py    # Continuous data producer
│
├── consumer/                    # Data consume karne wale scripts
│   ├── simple_consumer.py       # Basic consumer
│   └── druid_consumer.py        # Druid mein data push karne wala
│
├── config/                      # Configuration files
│   ├── kafka_config.py          # Kafka settings
│   └── druid_config.json        # Druid ingestion spec
│
├── data/                        # Sample data files
│   └── sample_products.json     # Product catalog data
│
└── docs/                        # Documentation
    ├── TASKS.md                 # All 7 tasks explained
    ├── SETUP_GUIDE.md           # Step-by-step setup
    └── TROUBLESHOOTING.md       # Common issues
```

---

## 🎓 Learning Tasks (From Screenshot)

### ✅ Task 1: Build a catalog of products
Create a product catalog and send to Kafka

### ✅ Task 2: Getting Started
Basic Kafka producer-consumer setup

### ✅ Task 3: Variables and Functions
Learn Python basics for Kafka

### ✅ Task 4: Recursion/Reusable
Create reusable Kafka functions

### ✅ Task 5: Create a Kafka Producer instance
Initialize Kafka producer properly

### ✅ Task 6: Send Records to Kafka Topic
Send data to Kafka topics

### ✅ Task 7: (From screenshot - not fully visible)
Advanced topics

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Dependencies
```bash
cd kafka-data-pipeline-project
pip install -r requirements.txt
```

### Step 2: Start Kafka (If Not Running)
```bash
cd ..
./start-kafka.sh
```

### Step 3: Run Simple Producer
```bash
cd kafka-data-pipeline-project
python producer/simple_producer.py
```

### Step 4: Run Simple Consumer (New Terminal)
```bash
cd kafka-data-pipeline-project
python consumer/simple_consumer.py
```

**Working? You'll see messages flowing! 🎉**

---

## 📚 What You'll Learn

### Beginner Level
- ✅ Python basics (variables, functions)
- ✅ Kafka producer setup
- ✅ Kafka consumer setup
- ✅ Sending/receiving messages
- ✅ JSON data handling

### Intermediate Level
- ✅ Confluent Kafka Python client
- ✅ Message serialization
- ✅ Error handling
- ✅ Continuous data streaming
- ✅ Data validation

### Advanced Level
- ✅ Druid integration
- ✅ Real-time analytics
- ✅ Grafana dashboards
- ✅ Production-ready code
- ✅ Performance optimization

---

## 🛠️ Technologies Used

| Technology | Purpose | Why? |
|------------|---------|------|
| **Python** | Programming language | Easy to learn, powerful |
| **Confluent Kafka** | Message broker | Industry standard, reliable |
| **Druid** | Analytics database | Fast queries, real-time |
| **Grafana** | Visualization | Beautiful dashboards |

---

## 📖 Detailed Guides

### For Complete Beginners:
1. Read `docs/TASKS.md` - Understand all 7 tasks
2. Read `docs/SETUP_GUIDE.md` - Step-by-step setup
3. Start with `producer/simple_producer.py` - Simplest example
4. Then try `producer/catalog_producer.py` - Real-world example

### For Quick Learners:
1. Install dependencies: `pip install -r requirements.txt`
2. Run producer: `python producer/simple_producer.py`
3. Run consumer: `python consumer/simple_consumer.py`
4. Modify and experiment!

---

## 🎯 Project Goals

By the end of this project, you will:
- ✅ Understand data pipelines
- ✅ Use Kafka for real-time data
- ✅ Write Python producer/consumer
- ✅ Integrate with Druid
- ✅ Create Grafana dashboards
- ✅ Build production-ready code

---

## 💡 Real-World Use Cases

### 1. E-commerce (Flipkart/Amazon)
```
Product Updates → Kafka → Druid → Grafana
(Price changes, inventory, orders)
```

### 2. Food Delivery (Zomato/Swiggy)
```
Delivery Tracking → Kafka → Druid → Grafana
(Location, status, ETA)
```

### 3. Ride Sharing (Ola/Uber)
```
Driver Location → Kafka → Druid → Grafana
(Real-time tracking, analytics)
```

---

## 🐛 Troubleshooting

### Issue 1: Kafka Not Running
```bash
# Check if Kafka is running
lsof -i :9092

# If not, start it
cd ..
./start-kafka.sh
```

### Issue 2: Module Not Found
```bash
# Install dependencies
pip install -r requirements.txt
```

### Issue 3: Connection Refused
```bash
# Check Kafka is on localhost:9092
# Verify in config/kafka_config.py
```

**More Help:** See `docs/TROUBLESHOOTING.md`

---

## 📞 Need Help?

1. Check `docs/TASKS.md` for task explanations
2. Check `docs/SETUP_GUIDE.md` for setup help
3. Check code comments (detailed Hinglish)
4. Check `docs/TROUBLESHOOTING.md` for issues

---

## 🎓 Learning Path

### Week 1: Basics
- Day 1-2: Setup & Task 1-2
- Day 3-4: Task 3-4
- Day 5-7: Task 5-6

### Week 2: Integration
- Day 1-3: Druid setup
- Day 4-5: Grafana dashboards
- Day 6-7: Testing & optimization

### Week 3: Advanced
- Build real project
- Add error handling
- Production deployment

---

## ✅ Success Checklist

### Setup Phase
- [ ] Kafka installed and running
- [ ] Python 3.8+ installed
- [ ] Dependencies installed
- [ ] Project structure created

### Learning Phase
- [ ] Task 1: Product catalog completed
- [ ] Task 2: Basic producer/consumer working
- [ ] Task 3: Variables & functions understood
- [ ] Task 4: Reusable code created
- [ ] Task 5: Producer instance working
- [ ] Task 6: Sending records successfully

### Integration Phase
- [ ] Druid installed
- [ ] Data flowing to Druid
- [ ] Grafana installed
- [ ] Dashboard created

### Completion
- [ ] End-to-end pipeline working
- [ ] Can explain each component
- [ ] Can modify and extend
- [ ] Ready for real projects

---

## 🌟 Next Steps After Completion

1. **Add More Data Sources**
   - Multiple producers
   - Different data types
   - Real APIs integration

2. **Enhance Analytics**
   - Complex Druid queries
   - Multiple Grafana dashboards
   - Alerting setup

3. **Production Ready**
   - Error handling
   - Logging
   - Monitoring
   - Docker deployment

---

## 📝 Notes

- **Language:** All code comments in Hinglish (Latin script only)
- **Difficulty:** Beginner to Intermediate
- **Time:** 2-3 weeks for complete mastery
- **Prerequisites:** Basic Python knowledge helpful but not required

---

**Happy Learning! 🚀**

_Agar koi doubt ho, to code comments padho - har line explain ki gayi hai!_
