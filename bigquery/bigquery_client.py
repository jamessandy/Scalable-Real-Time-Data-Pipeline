from google.cloud import bigquery
import json

def insert_into_bigquery(data):
    client = bigquery.Client()

    dataset_id = 'your-project-id.your_dataset'
    table_id = f'{dataset_id}.ecommerce_table'

    # Prepare the data for BigQuery
    rows_to_insert = [data]

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    
    if errors == []:
        print("Data successfully inserted into BigQuery.")
    else:
        print(f"Encountered errors: {errors}")

# Example usage: insert processed data into BigQuery
insert_into_bigquery({
    'user_id': 123,
    'product_id': 'A001',
    'category': 'electronics',
    'price': 49.99,
    'quantity': 3,
    'fraud_flag': False
})
