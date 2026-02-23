# Kafka Command Aliases - Complete Cheat Sheet

**Location**: `~/learningProjects/Learning-kafka-codewithDurgesh/.kafka-aliases`  
**Auto-loaded**: Yes (via `.zshrc`)  
**Bootstrap Server**: `localhost:19092` (Conduktor Docker)

---

## 📋 Quick Commands

### View Help
```bash
kafka-ref          # Quick reference guide
kafka-help         # Full list of aliases
kafka-info         # Environment information
```

---

## 📚 Topic Management (File 16)

### List Topics
```bash
kt-list                    # List all topics
kt-list-exclude            # List topics (exclude internal)
```

### Create Topics
```bash
kt-create --topic NAME --partitions 3              # Create with 3 partitions
kt-quick --topic NAME                              # Quick create (3 partitions default)
kt-create-show NAME 5                              # Create with 5 partitions and show details
```

### Describe & Manage
```bash
kt-describe --topic NAME                           # Show topic details
kt-alter --topic NAME --partitions 5               # Change partition count
kt-delete --topic NAME                             # Delete topic
```

**Examples:**
```bash
# Create a topic called "orders" with 3 partitions
kt-create --topic orders --partitions 3

# Describe it
kt-describe --topic orders

# Quick create and show
kt-create-show products 5
```

---

## 📤 Producer Commands (File 17)

### Basic Producer
```bash
kp --topic NAME                                    # Simple producer (no keys)
```
**Usage**: Type messages, press Enter. Exit with `Ctrl+C`

### Producer with Keys
```bash
kp-key --topic NAME                                # Producer with keys
```
**Usage**: Type in format `key:value`, press Enter

### Advanced Producers
```bash
kp-safe --topic NAME                               # Producer with acks=all (safe mode)
kp-rr --topic NAME                                 # Round-robin partitioner (testing)
kp-compress --topic NAME                           # Producer with gzip compression
```

**Examples:**
```bash
# Send simple messages
kp --topic orders
> Order 1
> Order 2
> ^C

# Send messages with keys
kp-key --topic users
> user1:John Doe
> user2:Jane Smith
> ^C

# Safe producer (production mode)
kp-safe --topic transactions
> Transaction 1
> ^C
```

---

## 📥 Consumer Commands (File 18)

### Basic Consumer
```bash
kc --topic NAME                                    # Read new messages only (tail mode)
kc-begin --topic NAME                              # Read from beginning (all history)
```

### Detailed Consumers
```bash
kc-detail --topic NAME --from-beginning            # Show key, partition, timestamp, value
kc-kv --topic NAME --from-beginning                # Show only keys and values
kc-partition --topic NAME --from-beginning         # Show partition and value
kc-time --topic NAME --from-beginning              # Show timestamp and value
```

### Consumer with Group
```bash
kc-group GROUP_NAME --topic NAME                   # Consumer with specific group
```

**Examples:**
```bash
# Read new messages (live tail)
kc --topic orders

# Read all messages from start
kc-begin --topic orders

# Read with full details
kc-detail --topic orders --from-beginning

# Output example:
# CreateTime:1732689123456 Partition:0 key1 value1
# CreateTime:1732689123789 Partition:1 key2 value2

# Consumer with group
kc-group my-app --topic orders --from-beginning
```

---

## 👥 Consumer Groups

### List & Describe
```bash
kcg-list                                           # List all consumer groups
kcg-describe --group NAME                          # Describe consumer group
```

### Reset Offsets
```bash
kcg-reset-begin --group NAME --topic TOPIC         # Reset to earliest
kcg-reset-end --group NAME --topic TOPIC           # Reset to latest
```

### Delete Group
```bash
kcg-delete --group NAME                            # Delete consumer group
```

**Examples:**
```bash
# List all groups
kcg-list

# Describe a group
kcg-describe --group my-app

# Reset group to beginning
kcg-reset-begin --group my-app --topic orders
```

---

## 🔧 System & Monitoring

### Cluster Management
```bash
kafka-status                                       # Check Kafka/Conduktor status
kafka-logs                                         # View Kafka logs (live)
kafka-start                                        # Start Kafka cluster
kafka-stop                                         # Stop Kafka cluster
kafka-restart                                      # Restart Kafka cluster
kafka-ui                                           # Open Conduktor UI (browser)
```

### Information
```bash
kafka-info                                         # Show environment info
```

**Examples:**
```bash
# Check if Kafka is running
kafka-status

# View logs
kafka-logs

# Open Conduktor dashboard
kafka-ui
```

---

## 🚀 Quick Workflows

### Test Workflow
```bash
kafka-test TOPIC_NAME                              # Create topic, produce, consume
```
**What it does:**
1. Creates topic with 3 partitions
2. Produces 3 test messages
3. Consumes and displays them

**Example:**
```bash
kafka-test demo
# Creates "demo" topic
# Sends: message1, message2, message3
# Shows output
```

---

## 📖 Complete Examples

### Example 1: Simple Message Flow
```bash
# 1. Create topic
kt-create --topic demo --partitions 2

# 2. Send messages (Terminal 1)
kp --topic demo
> Hello World
> Learning Kafka
> ^C

# 3. Read messages (Terminal 2)
kc-begin --topic demo
# Output:
# Hello World
# Learning Kafka
```

---

### Example 2: Messages with Keys
```bash
# 1. Create topic
kt-quick --topic users

# 2. Send with keys (Terminal 1)
kp-key --topic users
> user1:Alice
> user2:Bob
> user1:Alice Updated
> ^C

# 3. Read with details (Terminal 2)
kc-detail --topic users --from-beginning
# Output shows keys, partitions, timestamps
```

---

### Example 3: Consumer Groups
```bash
# 1. Create topic
kt-create --topic orders --partitions 3

# 2. Produce messages
echo -e "order1\norder2\norder3" | kp --topic orders

# 3. Consume with group (Terminal 1)
kc-group app1 --topic orders --from-beginning

# 4. Consume with same group (Terminal 2)
kc-group app1 --topic orders --from-beginning
# Messages will be distributed between consumers

# 5. Check group status
kcg-describe --group app1
```

---

## 🎯 Common Use Cases

### Development Testing
```bash
# Quick test a topic
kafka-test my-test-topic

# Create and immediately check
kt-create-show my-topic 3
```

### Debugging
```bash
# Check what's in a topic
kc-detail --topic my-topic --from-beginning

# Check consumer group lag
kcg-describe --group my-app

# View cluster status
kafka-status
```

### Production Simulation
```bash
# Safe producer
kp-safe --topic critical-data

# Consumer with group
kc-group production-app --topic critical-data
```

---

## 📝 Tips & Best Practices

1. **Always use `kt-list` before creating** to avoid duplicates
2. **Use `kp-safe` for important data** (acks=all)
3. **Use consumer groups** for scalable consumption
4. **Check `kafka-status`** before starting work
5. **Use `kc-detail`** for debugging partition/key issues

---

## 🔗 File References

| File | Topic | Aliases |
|------|-------|---------|
| 16. Kafka Topics CLI.md | Topic Management | `kt-*` |
| 17. Kafka Console Producer CLI.md | Producing Messages | `kp-*` |
| 18. Kafka Console Consumer CLI.md | Consuming Messages | `kc-*`, `kcg-*` |

---

## 🆘 Troubleshooting

### Aliases not working?
```bash
source ~/.zshrc
```

### Wrong port error?
Check: `echo $KAFKA_SERVER` should show `localhost:19092`

### Kafka not running?
```bash
kafka-status
kafka-start
```

### Need help?
```bash
kafka-ref          # Quick reference
kafka-help         # Full list
kafka-info         # Environment details
```

---

**Last Updated**: Nov 27, 2025  
**Kafka Version**: 4.1.1  
**Setup**: Conduktor Docker (Local)
