#!/bin/bash
echo "Listing all Kafka topics..."
/opt/homebrew/opt/kafka/bin/kafka-topics --list --bootstrap-server localhost:9092
