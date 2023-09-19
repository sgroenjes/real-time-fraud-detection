#!/bin/bash

# Navigate to your Kafka installation directory
cd /usr/bin/local/kafka/

# Start Zookeeper
nohup bin/zookeeper-server-start.sh config/zookeeper.properties > zookeeper.log 2>&1 &

# Give Zookeeper time to start
sleep 5

# Start Kafka server
nohup bin/kafka-server-start.sh config/server.properties > kafka.log 2>&1 &

# Create Kafka topic
bin/kafka-topics.sh --create --topic fraud_detection --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Navigate back to the project directory
cd -

echo "Kafka and Zookeeper started, topic 'fraud_detection' created."
