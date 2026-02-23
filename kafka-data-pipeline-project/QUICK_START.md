# ⚡ Quick Start Guide

> 5 minutes mein project chalu karo!

---

## 🚀 Super Quick (3 Commands)

```bash
# 1. Setup karo (one-time)
./setup.sh

# 2. Producer start karo
python3 producer/simple_producer.py

# 3. Consumer start karo (new terminal)
python3 consumer/simple_consumer.py
```

**Working? You're done! 🎉**

---

## 📋 Prerequisites

### Before Starting:
```bash
# 1. Kafka running hona chahiye
cd ..
./start-kafka.sh

# 2. Wait 10-15 seconds
# 3. Verify
lsof -i :9092  # Should show Kafka process
```

---

## 🎯 Task-wise Quick Start

### Task 1: Product Catalog
```bash
# Terminal 1
python3 producer/catalog_producer.py
# Choose option 3 (Quick test)

# Terminal 2
python3 consumer/simple_consumer.py
# See products flowing!
```

### Task 2: Getting Started
```bash
# Terminal 1
python3 producer/simple_producer.py

# Terminal 2
python3 consumer/simple_consumer.py
```

---

## 📁 Project Structure (Quick View)

```
kafka-data-pipeline-project/
├── producer/
│   ├── simple_producer.py       ← Start here (Task 2)
│   └── catalog_producer.py      ← Then this (Task 1)
├── consumer/
│   └── simple_consumer.py       ← Run this to see messages
├── config/
│   └── kafka_config.py          ← All settings here
└── docs/
    ├── TASKS.md                 ← All tasks explained
    ├── SETUP_GUIDE.md           ← Detailed setup
    └── TROUBLESHOOTING.md       ← If stuck
```

---

## 🐛 Quick Troubleshooting

### Problem: Connection Refused
```bash
# Solution: Start Kafka
cd ..
./start-kafka.sh
```

### Problem: Module Not Found
```bash
# Solution: Install dependencies
pip3 install -r requirements.txt
```

### Problem: No Messages
```bash
# Solution: Run producer first, then consumer
# Or consumer ko restart karo
```

---

## 📚 What to Read?

### Complete Beginner:
1. **README.md** (5 min) - Project overview
2. **docs/TASKS.md** (10 min) - Understand tasks
3. **Start coding!**

### Quick Learner:
1. **This file** (2 min)
2. **Run commands above**
3. **Experiment!**

---

## ✅ Success Checklist

- [ ] Kafka running (`lsof -i :9092`)
- [ ] Dependencies installed (`./setup.sh`)
- [ ] Producer runs without errors
- [ ] Consumer receives messages
- [ ] You understand the flow

---

## 🎓 Learning Path

```
Day 1: simple_producer.py + simple_consumer.py
       ↓
Day 2: catalog_producer.py (Product catalog)
       ↓
Day 3: Modify and experiment
       ↓
Day 4+: Build your own project!
```

---

## 💡 Pro Tips

1. **Always start Kafka first**
2. **Run consumer before producer** (to see all messages)
3. **Read code comments** (detailed Hinglish explanations)
4. **Experiment** (change values, see what happens)
5. **Check docs/** folder when stuck

---

## 🆘 Need Help?

**Quick Help:**
- Check `docs/TROUBLESHOOTING.md`
- Read code comments
- Check Kafka logs: `tail -f /opt/homebrew/var/log/kafka/server.log`

**Detailed Help:**
- `README.md` - Complete overview
- `docs/TASKS.md` - Task explanations
- `docs/SETUP_GUIDE.md` - Detailed setup

---

**Ready? Run `./setup.sh` now! 🚀**
