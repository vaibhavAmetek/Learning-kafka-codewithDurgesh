#!/bin/bash
TOPIC_NAME=${1:-"quickstart-events"}
echo "Starting Kafka Consumer for topic: $TOPIC_NAME"
/opt/homebrew/opt/kafka/bin/kafka-console-consumer --topic $TOPIC_NAME --from-beginning --bootstrap-server localhost:9092
