# Real-Time Fraud Detection System

## Overview

This project aims to build a real-time fraud detection system using Apache Kafka for data ingestion and Apache Spark for data processing and machine learning.

## Technologies Used

- Apache Kafka
- Apache Spark
- Python

## Setup

### Apache Kafka

1. **Download and Install Apache Kafka**: [Official Website](https://kafka.apache.org/downloads)

2. **Start Zookeeper and Kafka Server**: Run the `start-kafka.sh` script to start Zookeeper and Kafka Server.

    ```bash
    ./start-kafka.sh
    ```

3. **Create Kafka Topic**: The `start-kafka.sh` script will automatically create a topic named `fraud_detection`.

### Python Environment

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the data producer script:

    ```bash
    python data_producer.py
    ```

## How to Run

1. Start Kafka:

    ```bash
    ./start-kafka.sh
    ```

2. Run the data producer script:

    ```bash
    python data_producer.py
    ```

3. (Future Steps) Run the Spark Streaming job:

    ```bash
    # Command here
    ```

## Author

Sam Groenjes