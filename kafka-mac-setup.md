# Apache Kafka Setup Guide for macOS (Hinglish)

---

## Kafka Kya Hai? (Quick Overview)

**Apache Kafka** ek **distributed event streaming platform** hai jo Fortune 100 companies ke **80%** use karte hain.

### Key Industries Using Kafka:

- **Manufacturing**: 10 out of 10 companies
- **Banks**: 7 out of 10 companies
- **Insurance**: 10 out of 10 companies
- **Telecom**: 8 out of 10 companies

### Kafka Ki Teen Main Capabilities:

```
1. PUBLISH (Write)
   └─> Events ko Kafka topics mein bhejo

2. STORE (Durably)
   └─> Events ko reliably store karo (as long as you want)

3. PROCESS (Real-time)
   └─> Events ko process karo jab wo occur ho rahe hon
```

**Use Cases:**

- High-performance data pipelines
- Streaming analytics
- Data integration
- Mission-critical applications

---

## Installation Steps Summary (From Video)

```
Installation Process:

1. Download Kafka zip file from official website
   └─> https://kafka.apache.org/downloads

2. Extract file
   └─> Unzip the downloaded archive

3. Start Zookeeper
   └─> Coordination service (for older Kafka versions)

4. Start Kafka Server
   └─> Main Kafka broker
```

---

## Kafka Storage Architecture (Image 4 Explanation)

### Topic aur Partition Structure:

```
STORAGE SYSTEM:

TOPIC (Logical Container)
  |
  +-- P1 (Partition 1): [■][■][■][■][ ]  <-- Producer Client 1 (Phone)
  |                      ↑
  |                   Event sent and appended
  |
  +-- P2 (Partition 2): [■][■][■][■][ ]
  |
  +-- P3 (Partition 3): [■][■][■][■][ ]  <-- Producer Client 2 (Car)
  |
  +-- P4 (Partition 4): [■][■][■][■][ ]
```

**Key Points:**

- **Colored boxes (■)**: Filled storage slots (messages stored)
- **Empty boxes ( )**: Available storage space
- **Same color = Same key**: Events with same key go to same partition
- **Order guaranteed**: Within partition, messages ordered hain
- **Two producers**: Independently publish kar sakte hain (phone aur car)

**Important**: Events with same key (denoted by color) always same partition mein jayenge. Order preservation ke liye zaroori hai.

---

## Kafka APIs (Image 5 Explanation)

### 1. Admin API

**Purpose**: Manage and inspect Kafka objects

```
Use Cases:
- Topics create/delete
- Brokers inspect
- Configurations manage
```

### 2. Producer API

**Purpose**: Publish (write) events to Kafka topics

```
Example:
Driver location send karna
User actions log karna
```

### 3. Consumer API

**Purpose**: Subscribe to (read) topics and process events

```
Example:
Messages read karna
Data process karna
Database update karna
```

### 4. Kafka Streams API

**Purpose**: Stream processing applications

```
Features:
- Transformations
- Stateful operations (aggregations, joins)
- Windowing operations
- Event-time processing

Input: Read from topics
Output: Write to topics (transformed data)
```

### 5. Kafka Connect API

**Purpose**: Build reusable data import/export connectors

```
Example:
- PostgreSQL connector (database changes capture)
- MongoDB connector
- Elasticsearch connector
- S3 connector

Note: Ready-to-use connectors already available (implement karne ki zarurat nahi)
```

---

## Prerequisites

Before starting, ensure you have:

- **Java 17 or higher** installed
- **Homebrew** (recommended for easy installation)

### System Requirements:

- **Operating System**: macOS 10.15+ (Catalina or later)
- **Java**: Version 17 or higher (JDK)
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: At least 2GB free
- **Terminal**: Knowledge of basic commands

### Check Java Version

```bash
java -version
```

**Expected Output:**

```
openjdk version "17.0.x" or higher
```

If you don't have Java 17+, install it:

```bash
# Using Homebrew (Recommended)
brew install openjdk@17

# Set JAVA_HOME environment variable
echo 'export JAVA_HOME="/opt/homebrew/opt/openjdk@17"' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc

# Apply changes
source ~/.zshrc

# Verify installation
java -version
```

---

## 🚀 Quick Install (Using Automated Script)

**Easiest Method**: Use kar automated installation script

### Step 1: Download aur Run Script

```bash
# Script ko executable banao
chmod +x install-kafka-mac.sh

# Script run karo
./install-kafka-mac.sh
```

### Script Kya Karega:

```
✅ Operating System check karega
✅ Homebrew install/check karega
✅ Java 17+ install karega (agar nahi hai)
✅ Kafka install karega via Homebrew
✅ KRaft mode configure karega (no Zookeeper needed)
✅ Helper scripts create karega:
   - start-kafka.sh
   - stop-kafka.sh
   - create-topic.sh
   - list-topics.sh
   - start-producer.sh
   - start-consumer.sh
```

### After Installation:

```bash
# 1. Kafka start karo
./start-kafka.sh

# 2. Naye terminal mein topic create karo
./create-topic.sh my-first-topic

# 3. Producer start karo
./start-producer.sh my-first-topic

# 4. Another terminal mein consumer start karo
./start-consumer.sh my-first-topic

# 5. Topics list dekho
./list-topics.sh

# 6. Kafka stop karo
./stop-kafka.sh
```

---

## Method 1: Install Using Homebrew (Manual)

This is the easiest way to install Kafka on Mac.

### Step 1: Install Kafka

```bash
brew install kafka
```

This will automatically install Kafka and its dependency (ZooKeeper, though Kafka 4.x uses KRaft mode by default).

### Step 2: Start Kafka Service

Kafka is installed at `/opt/homebrew/opt/kafka` (Apple Silicon) or `/usr/local/opt/kafka` (Intel Mac).

**Start Kafka in KRaft mode (standalone):**

```bash
# Generate Cluster UUID
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"

# Format the log directories
kafka-storage format --standalone -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/kraft/server.properties

# Start Kafka server
kafka-server-start /opt/homebrew/etc/kafka/kraft/server.properties
```

**Or start as a background service:**

```bash
brew services start kafka
```

### Step 3: Verify Kafka is Running

Open a new terminal and check if Kafka is listening on port 9092:

```bash
lsof -i :9092
```

---

## Method 2: Manual Installation (Downloaded Files)

### Step 1: Download Kafka

```bash
# Create a directory for Kafka
mkdir ~/kafka && cd ~/kafka

# Download Kafka (using curl)
curl -O https://downloads.apache.org/kafka/4.1.1/kafka_2.13-4.1.1.tgz

# Extract the archive
tar -xzf kafka_2.13-4.1.1.tgz
cd kafka_2.13-4.1.1
```

### Step 2: Start Kafka Environment

```bash
# Generate a Cluster UUID
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

# Format Log Directories
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties

# Start the Kafka Server
bin/kafka-server-start.sh config/server.properties
```

---

## Method 3: Using Docker (Cross-platform)

If you prefer Docker:

### Step 1: Install Docker Desktop for Mac

Download from: https://www.docker.com/products/docker-desktop

### Step 2: Run Kafka Container

```bash
# Pull the Kafka image
docker pull apache/kafka:4.1.1

# Start Kafka
docker run -p 9092:9092 apache/kafka:4.1.1
```

---

## Working with Kafka

Once Kafka is running, open **new terminal windows** for the following commands:

### Create a Topic

```bash
# If using Homebrew
kafka-topics --create --topic quickstart-events --bootstrap-server localhost:9092

# If using manual installation (from kafka directory)
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
```

### Describe the Topic

```bash
kafka-topics --describe --topic quickstart-events --bootstrap-server localhost:9092
```

### Produce Messages (Write Events)

```bash
# Start the producer
kafka-console-producer --topic quickstart-events --bootstrap-server localhost:9092

# Then type your messages (press Enter after each):
> Hello from Mac!
> This is my first Kafka event
> Testing Kafka on macOS

# Press Ctrl-C to exit
```

### Consume Messages (Read Events)

Open another terminal and run:

```bash
kafka-console-consumer --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```

You should see all the messages you produced!

---

## Useful Commands

### List All Topics

```bash
kafka-topics --list --bootstrap-server localhost:9092
```

### Delete a Topic

```bash
kafka-topics --delete --topic quickstart-events --bootstrap-server localhost:9092
```

### Check Kafka Logs (Homebrew installation)

```bash
tail -f /opt/homebrew/var/log/kafka/server.log
```

---

## Stopping Kafka

### If Running in Terminal

Press `Ctrl-C` in the terminal where Kafka is running.

### If Running as Homebrew Service

```bash
brew services stop kafka
```

### Clean Up Data (Optional)

```bash
# For Homebrew installation
rm -rf /opt/homebrew/var/lib/kraft-combined-logs

# For manual installation
rm -rf /tmp/kafka-logs /tmp/kraft-combined-logs
```

---

## Common Issues on Mac

### Issue 1: Port 9092 Already in Use

```bash
# Find what's using the port
lsof -i :9092

# Kill the process (replace PID with actual process ID)
kill -9 PID
```

### Issue 2: Java Not Found

Make sure Java 17+ is installed and in your PATH:

```bash
java -version
echo $JAVA_HOME
```

If `JAVA_HOME` is not set:

```bash
# Add to ~/.zshrc
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
source ~/.zshrc
```

### Issue 3: Permission Denied

If you get permission errors with Homebrew:

```bash
sudo chown -R $(whoami) /opt/homebrew/var/lib/kafka-logs
```

---

## Next Steps

1. **Explore Kafka Connect** - Import/export data from files or databases
2. **Try Kafka Streams** - Process real-time data streams
3. **Build a Java/Spring Boot application** - Integrate Kafka with your backend
4. **Set up multiple brokers** - Create a Kafka cluster

---

## Quick Reference

| Command      | Homebrew                     | Manual Installation                                  |
| ------------ | ---------------------------- | ---------------------------------------------------- |
| Start Kafka  | `brew services start kafka`  | `bin/kafka-server-start.sh config/server.properties` |
| Stop Kafka   | `brew services stop kafka`   | `Ctrl-C`                                             |
| Create Topic | `kafka-topics --create ...`  | `bin/kafka-topics.sh --create ...`                   |
| Producer     | `kafka-console-producer ...` | `bin/kafka-console-producer.sh ...`                  |
| Consumer     | `kafka-console-consumer ...` | `bin/kafka-console-consumer.sh ...`                  |

---

**Congratulations!** You now have Kafka running on your Mac. Happy streaming! 🚀
