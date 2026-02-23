# Kafka Commands - Easy Reference Guide

## 🎯 Command Simplification

### Before (Long Commands) ❌
```bash
# Local Docker
kafka-topics --bootstrap-server localhost:19092 --list
kafka-console-producer --bootstrap-server localhost:19092 --topic my-topic
kafka-console-consumer --bootstrap-server localhost:19092 --topic my-topic --from-beginning

# Conduktor Cloud
kafka-topics --command-config playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --list
kafka-console-producer --producer.config playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic my-topic
```

### After (With Aliases) ✅
```bash
# Local Docker
kt-list
kp --topic my-topic
kc-begin --topic my-topic

# Conduktor Cloud
ktc-list
kpc --topic my-topic
kcc-begin --topic my-topic
```

---

## 📊 Command Comparison Table

| Operation | Local (Docker) | Cloud | Full Command (Local) |
|-----------|----------------|-------|----------------------|
| **List Topics** | `kt-list` | `ktc-list` | `kafka-topics --bootstrap-server localhost:19092 --list` |
| **Create Topic** | `kt-create --topic NAME --partitions 3` | `ktc-create --topic NAME --partitions 3` | `kafka-topics --bootstrap-server localhost:19092 --create --topic NAME --partitions 3` |
| **Describe Topic** | `kt-describe --topic NAME` | `ktc-describe --topic NAME` | `kafka-topics --bootstrap-server localhost:19092 --describe --topic NAME` |
| **Delete Topic** | `kt-delete --topic NAME` | `ktc-delete --topic NAME` | `kafka-topics --bootstrap-server localhost:19092 --delete --topic NAME` |
| **Produce Messages** | `kp --topic NAME` | `kpc --topic NAME` | `kafka-console-producer --bootstrap-server localhost:19092 --topic NAME` |
| **Produce with Keys** | `kp-key --topic NAME` | `kpc-key --topic NAME` | `kafka-console-producer --bootstrap-server localhost:19092 --property parse.key=true --property key.separator=: --topic NAME` |
| **Consume (Tail)** | `kc --topic NAME` | `kcc --topic NAME` | `kafka-console-consumer --bootstrap-server localhost:19092 --topic NAME` |
| **Consume (All)** | `kc-begin --topic NAME` | `kcc-begin --topic NAME` | `kafka-console-consumer --bootstrap-server localhost:19092 --topic NAME --from-beginning` |
| **Consume (Details)** | `kc-detail --topic NAME` | `kcc-detail --topic NAME` | `kafka-console-consumer --bootstrap-server localhost:19092 --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --property print.partition=true --topic NAME` |
| **List Groups** | `kcg-list` | `kcgc-list` | `kafka-consumer-groups --bootstrap-server localhost:19092 --list` |
| **Describe Group** | `kcg-describe --group NAME` | `kcgc-describe --group NAME` | `kafka-consumer-groups --bootstrap-server localhost:19092 --describe --group NAME` |

---

## 🔑 Pattern Recognition

### Naming Convention:
```
k     = Kafka
t/p/c = Topic/Producer/Consumer
c     = Cloud (suffix)
```

### Examples:
- `kt` = Kafka Topics (local)
- `ktc` = Kafka Topics Cloud
- `kp` = Kafka Producer (local)
- `kpc` = Kafka Producer Cloud
- `kc` = Kafka Consumer (local)
- `kcc` = Kafka Consumer Cloud
- `kcg` = Kafka Consumer Groups (local)
- `kcgc` = Kafka Consumer Groups Cloud

---

## 💡 Quick Usage Examples

### Local Docker (Default)
```bash
# Create and test topic
kt-create --topic demo --partitions 3
kt-describe --topic demo

# Produce messages
kp --topic demo
> Hello World
> Message 2
> ^C (Ctrl+C to exit)

# Consume messages
kc-begin --topic demo
```

### Conduktor Cloud
```bash
# First, configure playground.config with your credentials
# Then use same commands with 'c' suffix

ktc-list
kpc --topic demo
kcc-begin --topic demo
```

---

## 🚀 Advanced Examples

### Producer with Keys (Local)
```bash
kp-key --topic study
> user1:Login successful
> user2:Purchase completed
> user1:Logout
```

### Consumer with Full Details (Local)
```bash
kc-detail --topic study --from-beginning
# Output shows: Timestamp | Partition | Key | Value
```

### Consumer Groups (Local)
```bash
# Create consumer with group
kc-group my-app --topic study --from-beginning

# Check group status
kcg-describe --group my-app

# Reset offsets
kcg-reset-begin --group my-app --topic study
```

---

## 📝 Environment Variables

Your aliases use these variables (defined in `~/.kafka-aliases`):

```bash
KAFKA_SERVER="localhost:19092"              # Local Docker
KAFKA_CLOUD_SERVER="cluster.playground.cdkt.io:9092"  # Cloud
KAFKA_CONFIG="~/learningProjects/Learning-kafka-codewithDurgesh/playground.config"
```

---

## 🔧 System Commands

```bash
kafka-status    # Check Docker containers
kafka-ui        # Open Conduktor UI (http://localhost:8080)
kafka-info      # Show environment details
kafka-test demo # Quick test workflow
kafka-ref       # This quick reference
kafka-help      # All aliases
kafka-cheat     # Full documentation
```

---

## 📚 Setup Conduktor Cloud

1. **Get Credentials**: https://console.conduktor.io/ → My Playground → Connection Details

2. **Edit `playground.config`**:
```properties
security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="YOUR_USERNAME" password="YOUR_PASSWORD";
```

3. **Test Connection**:
```bash
ktc-list
```

---

## ⚡ Time Saved

| Task | Before | After | Saved |
|------|--------|-------|-------|
| List topics | 58 chars | 7 chars | **88% less typing** |
| Create topic | 95 chars | 35 chars | **63% less typing** |
| Produce messages | 70 chars | 15 chars | **79% less typing** |
| Consume from beginning | 98 chars | 25 chars | **75% less typing** |

**Average: 76% less typing!** 🎉

---

## 🎓 Learning Path

1. **Start Local**: Use `kt-*`, `kp`, `kc` commands with Docker
2. **Practice**: Create topics, produce/consume messages
3. **Try Cloud**: Configure `playground.config` and use `ktc-*`, `kpc`, `kcc`
4. **Advanced**: Consumer groups, keys, partitions, offsets

---

## 🆘 Troubleshooting

### Aliases not working?
```bash
source ~/.kafka-aliases
```

### Cloud commands failing?
```bash
# Check config file
cat ~/learningProjects/Learning-kafka-codewithDurgesh/playground.config

# Verify credentials at: https://console.conduktor.io/
```

### Docker not running?
```bash
kafka-status    # Check status
kafka-start     # Start cluster
```

---

**Happy Kafka Learning! 🚀**

For detailed notes, check: `complete-guide-to-apache-kafka-for-beginners/` folder
