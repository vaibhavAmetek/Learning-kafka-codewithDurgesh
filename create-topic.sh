#!/bin/bash
TOPIC_NAME=${1:-"quickstart-events"}
PARTITIONS=${2:-3}
REPLICATION=${3:-1}
echo "Creating topic: $TOPIC_NAME with $PARTITIONS partitions and replication factor $REPLICATION"
/opt/homebrew/opt/kafka/bin/kafka-topics --create --topic $TOPIC_NAME --bootstrap-server localhost:9092 --partitions $PARTITIONS --replication-factor $REPLICATION
echo "Topic created successfully!"
