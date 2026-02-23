# 🎯 Kafka Command Aliases - Complete Setup

## ✅ What's Installed

You now have **60+ Kafka command aliases** that make working with Kafka super easy!

---

## 📚 Documentation Files

| File | Purpose | Command to View |
|------|---------|-----------------|
| `KAFKA_QUICK_COMMANDS.md` | Quick reference (1 page) | `cat KAFKA_QUICK_COMMANDS.md` |
| `KAFKA_COMMAND_COMPARISON.md` | Before/After comparison | `cat KAFKA_COMMAND_COMPARISON.md` |
| `~/KAFKA_CHEATSHEET.md` | Full documentation | `kafka-cheat` |
| `.kafka-aliases` | Alias definitions | `cat ~/.kafka-aliases` |

---

## 🚀 Quick Start

### 1. Check Setup
```bash
kafka-info    # Shows environment details
kafka-ref     # Quick command reference
```

### 2. Local Docker Commands
```bash
# Topics
kt-list                              # List all topics
kt-create --topic demo --partitions 3    # Create topic
kt-describe --topic demo             # Show details

# Producer (Terminal 1)
kp --topic demo
> Hello World
> Message 2
> ^C

# Consumer (Terminal 2)
kc-begin --topic demo
```

### 3. Cloud Commands (Same but add 'c')
```bash
ktc-list                             # List cloud topics
kpc --topic demo                     # Cloud producer
kcc-begin --topic demo               # Cloud consumer
```

---

## 🎨 Command Pattern

```
┌─────────────────────────────────────┐
│  LOCAL vs CLOUD - Just add 'c'!    │
├─────────────────────────────────────┤
│  kt-list    →    ktc-list          │
│  kp         →    kpc                │
│  kc         →    kcc                │
│  kcg-list   →    kcgc-list          │
└─────────────────────────────────────┘
```

---

## 📋 All Available Commands

### Topics (kt-*)
```bash
kt-list              # List all topics
kt-list-exclude      # List (exclude internal)
kt-create            # Create topic
kt-describe          # Describe topic
kt-delete            # Delete topic
kt-alter             # Alter topic
kt-quick             # Quick create (3 partitions)

# Cloud versions: ktc-*
```

### Producer (kp-*)
```bash
kp                   # Basic producer
kp-key               # Producer with keys (key:value)
kp-safe              # Producer with acks=all
kp-rr                # Round-robin partitioner
kp-compress          # With gzip compression

# Cloud versions: kpc, kpc-key
```

### Consumer (kc-*)
```bash
kc                   # Tail mode (new messages)
kc-begin             # From beginning (all history)
kc-detail            # With timestamp, key, partition
kc-kv                # Key => Value format
kc-partition         # With partition info
kc-time              # With timestamp
kc-group             # With consumer group

# Cloud versions: kcc, kcc-begin, kcc-detail
```

### Consumer Groups (kcg-*)
```bash
kcg-list             # List all groups
kcg-describe         # Describe group
kcg-reset-begin      # Reset to earliest
kcg-reset-end        # Reset to latest
kcg-delete           # Delete group

# Cloud versions: kcgc-*
```

### System Commands
```bash
kafka-status         # Check Docker containers
kafka-logs           # View Kafka logs
kafka-restart        # Restart cluster
kafka-stop           # Stop cluster
kafka-start          # Start cluster
kafka-ui             # Open Conduktor UI
```

### Helper Commands
```bash
kafka-ref            # Quick reference
kafka-help           # All aliases
kafka-cheat          # Full cheatsheet
kafka-info           # Environment info
kafka-test TOPIC     # Quick test workflow
kt-create-show       # Create + describe
```

---

## 💡 Common Use Cases

### 1. Quick Topic Test
```bash
kafka-test demo
```

### 2. Create Topic with Details
```bash
kt-create-show study 5    # 5 partitions
```

### 3. Producer with Keys
```bash
kp-key --topic study
> user1:Login successful
> user2:Purchase completed
> user1:Logout
```

### 4. Consumer with Full Details
```bash
kc-detail --topic study --from-beginning
```

### 5. Consumer Group Workflow
```bash
# Terminal 1: Start consumer in group
kc-group my-app --topic demo --from-beginning

# Terminal 2: Check group status
kcg-describe --group my-app

# Terminal 3: Another consumer in same group
kc-group my-app --topic demo --from-beginning
```

### 6. Filter Your Topics Only
```bash
kt-list | grep -v "^_"    # Exclude internal topics
```

---

## ⚙️ Setup Conduktor Cloud (Optional)

If you want to use cloud commands (`ktc-*`, `kpc`, `kcc`):

### Step 1: Get Credentials
1. Go to: https://console.conduktor.io/
2. Navigate to: **My Playground** → **Connection Details**
3. Copy your username and password

### Step 2: Configure File
Edit `playground.config`:
```properties
security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="YOUR_USERNAME" password="YOUR_PASSWORD";
```

### Step 3: Test
```bash
ktc-list    # Should show cloud topics
```

---

## 🔧 Troubleshooting

### Aliases not working?
```bash
source ~/.zshrc
# or
source ~/.kafka-aliases
```

### Check if aliases loaded?
```bash
type kt-list    # Should show alias definition
```

### Docker not running?
```bash
kafka-status    # Check status
kafka-start     # Start if needed
```

### Cloud commands failing?
```bash
# Verify config file exists
cat ~/learningProjects/Learning-kafka-codewithDurgesh/playground.config

# Check credentials at: https://console.conduktor.io/
```

---

## 📊 Time Saved

Before:
```bash
kafka-topics --bootstrap-server localhost:19092 --list
# 58 characters
```

After:
```bash
kt-list
# 7 characters - 88% less typing! 🎉
```

---

## 🎓 Learning Resources

| Topic | File Location |
|-------|---------------|
| Kafka Basics | `complete-guide-to-apache-kafka-for-beginners/01_Apache_Kafka_Introduction_5min.md` |
| Topics CLI | `complete-guide-to-apache-kafka-for-beginners/16. Kafka Topics CLI.md` |
| Producer CLI | `complete-guide-to-apache-kafka-for-beginners/17. Kafka Console Producer CLI.md` |
| Consumer CLI | `complete-guide-to-apache-kafka-for-beginners/18. Kafka Console Consumer CLI.md` |
| Setup Guide | `complete-guide-to-apache-kafka-for-beginners/14. Setting up Kafka on macOS.md` |

---

## 🚀 Next Steps

1. **Practice Local**: Use `kt-*`, `kp`, `kc` commands
2. **Try Workflows**: Producer → Consumer, Consumer Groups
3. **Setup Cloud**: Configure `playground.config` for cloud practice
4. **Advanced Topics**: Keys, Partitions, Offsets, Consumer Groups

---

## 📞 Quick Help

```bash
kafka-ref     # Quick reference in terminal
kafka-cheat   # Full documentation with pager
kafka-info    # Your current setup
kafka-help    # All aliases list
```

---

**Happy Kafka Learning! 🎉**

Created by: Cascade AI Assistant
Date: Nov 27, 2025
Version: 2.0 (with Cloud support)
