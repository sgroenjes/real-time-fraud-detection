from kafka import KafkaProducer
import json
import random
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Load your dataset here (e.g., a CSV file from Kaggle)
# For demonstration, let's assume each transaction is a dictionary with 'amount' and 'is_fraud' keys
transactions = [
    {'amount': 100, 'is_fraud': 0},
    {'amount': 2000, 'is_fraud': 1},
    # Add more transactions
]

while True:
    transaction = random.choice(transactions)
    producer.send('fraud_detection', value=transaction)
    time.sleep(1)  # Simulate a delay
