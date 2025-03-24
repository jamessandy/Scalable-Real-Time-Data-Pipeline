from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import MapFunction

class FraudDetectionMapFunction(MapFunction):
    def map(self, value):
        # Example logic to detect fraud: If quantity > 10, flag as fraud
        if value['quantity'] > 10:
            value['fraud_flag'] = True
        else:
            value['fraud_flag'] = False
        return value

# Initialize the Flink execution environment
env = StreamExecutionEnvironment.get_execution_environment()

# Read data from Kafka
data_stream = env.add_source(
    KafkaSource.builder()
    .set_bootstrap_servers('localhost:9092')
    .set_topics('ecommerce_topic')
    .set_group_id('flink-group')
    .set_value_only_deserializer(SimpleStringSchema())
    .build()
)

# Apply the fraud detection logic
processed_stream = data_stream.map(FraudDetectionMapFunction())

# Sink processed data to BigQuery (or any other sink)
processed_stream.add_sink(MyBigQuerySink())

# Execute the job
env.execute("Ecommerce Real-Time Data Pipeline")
