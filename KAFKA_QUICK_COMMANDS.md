# ⚡ Kafka Quick Commands Cheatsheet

## 🎯 Pattern: Add 'c' for Cloud

```
Local:  kt-list    kp --topic X    kc-begin --topic X
Cloud:  ktc-list   kpc --topic X   kcc-begin --topic X
        ↑                ↑                  ↑
        Add 'c' suffix for cloud commands!
```

---

## 📋 Topics

```bash
# LOCAL                          # CLOUD
kt-list                          ktc-list
kt-create --topic X --partitions 3    ktc-create --topic X --partitions 3
kt-describe --topic X            ktc-describe --topic X
kt-delete --topic X              ktc-delete --topic X
```

---

## 📤 Producer

```bash
# LOCAL                          # CLOUD
kp --topic X                     kpc --topic X
kp-key --topic X                 kpc-key --topic X
kp-safe --topic X                # (use kpc with acks=all)

# Usage:
kp --topic demo
> Hello World
> Message 2
> ^C (Ctrl+C to exit)
```

---

## 📥 Consumer

```bash
# LOCAL                          # CLOUD
kc --topic X                     kcc --topic X
kc-begin --topic X               kcc-begin --topic X
kc-detail --topic X              kcc-detail --topic X
kc-group my-app --topic X        # (use kcc with --group)
```

---

## 👥 Consumer Groups

```bash
# LOCAL                          # CLOUD
kcg-list                         kcgc-list
kcg-describe --group X           kcgc-describe --group X
kcg-reset-begin --group X --topic Y
kcg-delete --group X
```

---

## 🔧 System

```bash
kafka-status     # Check Docker
kafka-ui         # Open UI (localhost:8080)
kafka-info       # Show config
kafka-test demo  # Quick test
kafka-ref        # This guide
kafka-cheat      # Full docs
```

---

## 🚀 Common Workflows

### 1. Create & Test Topic
```bash
kt-create --topic demo --partitions 3
kt-describe --topic demo
kafka-test demo
```

### 2. Producer → Consumer
```bash
# Terminal 1: Producer
kp --topic demo
> Message 1
> Message 2

# Terminal 2: Consumer
kc-begin --topic demo
```

### 3. With Keys
```bash
# Terminal 1: Producer with keys
kp-key --topic study
> user1:Login
> user2:Purchase
> user1:Logout

# Terminal 2: Consumer with details
kc-detail --topic study --from-beginning
```

### 4. Consumer Groups
```bash
# Terminal 1: Consumer in group
kc-group app1 --topic demo --from-beginning

# Terminal 2: Check group
kcg-describe --group app1
```

---

## 💡 Pro Tips

1. **Filter Internal Topics**:
   ```bash
   kt-list | grep -v "^_"
   ```

2. **Count Topics**:
   ```bash
   kt-list | wc -l
   ```

3. **Quick Topic Info**:
   ```bash
   kt-describe --topic study
   ```

4. **Test Connection**:
   ```bash
   kafka-test my-topic
   ```

5. **View Logs**:
   ```bash
   kafka-logs
   ```

---

## 🔑 Remember

| Prefix | Meaning | Example |
|--------|---------|---------|
| `kt` | Kafka Topics | `kt-list` |
| `kp` | Kafka Producer | `kp --topic X` |
| `kc` | Kafka Consumer | `kc-begin --topic X` |
| `kcg` | Kafka Consumer Groups | `kcg-list` |
| `*c` | Cloud suffix | `ktc-list`, `kpc`, `kcc` |

---

## ⚙️ Setup Cloud (One-time)

1. Get credentials: https://console.conduktor.io/
2. Edit `playground.config`:
   ```properties
   security.protocol=SASL_SSL
   sasl.mechanism=PLAIN
   sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="YOUR_USER" password="YOUR_PASS";
   ```
3. Test: `ktc-list`

---

**Print this and keep it handy! 📌**
