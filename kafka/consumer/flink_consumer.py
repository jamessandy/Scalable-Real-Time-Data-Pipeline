from kafka import KafkaConsumer
import json
import logging

# Set up Kafka consumer
consumer = KafkaConsumer(
    'ecommerce_topic',
    bootstrap_servers=['localhost:9092'],  # Adjust based on your Kafka setup
    group_id='flink-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Process the incoming messages
for message in consumer:
    data = message.value
    print(f"Consumed message: {data}")
    # Here, you can send this data to Flink or process it directly
