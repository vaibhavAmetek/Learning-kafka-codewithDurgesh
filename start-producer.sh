#!/bin/bash
TOPIC_NAME=${1:-"quickstart-events"}
echo "Starting Kafka Producer for topic: $TOPIC_NAME"
echo "Type your messages (Ctrl+C to exit):"
/opt/homebrew/opt/kafka/bin/kafka-console-producer --topic $TOPIC_NAME --bootstrap-server localhost:9092
