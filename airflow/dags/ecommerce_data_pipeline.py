from airflow import DAG
from airflow.providers.kafka.operators.kafka_producer import KafkaProducerOperator
from airflow.providers.apache.flink.operators.flink import FlinkOperator
from datetime import datetime

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 13),
    'retries': 1,
}

# Define the DAG
with DAG('ecommerce_data_pipeline', default_args=default_args, schedule_interval='@hourly') as dag:
    # Kafka producer task
    produce_data = KafkaProducerOperator(
        task_id='produce_data',
        kafka_conn_id='kafka_default',  # Set this connection in Airflow's UI
        topic='ecommerce_topic',
        value="{{ task_instance.xcom_pull(task_ids='produce_data') }}",
        provide_context=True
    )
    
    # Flink processing task
    flink_task = FlinkOperator(
        task_id='flink_process',
        flink_version='1.13',
        java_class='com.flink.EcommerceProcessor',  # Update with your Flink job class
        job_manager_memory='1024m',
        task_manager_memory='1024m',
        flink_conn_id='flink_default'
    )

    # Set task dependencies
    produce_data >> flink_task
