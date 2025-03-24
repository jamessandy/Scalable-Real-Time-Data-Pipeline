from kafka import KafkaProducer
import pandas as pd
import json

# Load the e-commerce dataset (CSV)
df = pd.read_csv('data/ecommerce_data.csv')

# Set up Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Adjust based on your Kafka setup
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Stream the data row by row to Kafka
for index, row in df.iterrows():
    data = {
        'user_id': row['User ID'],
        'product_id': row['Product ID'],
        'category': row['Category'],
        'price': row['Price'],
        'quantity': row['Quantity'],
        'timestamp': row['Timestamp'],
    }
    producer.send('ecommerce_topic', value=data)
    print(f"Produced message: {data}")

# Close producer
producer.flush()
producer.close()
