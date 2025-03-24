# Use an official Airflow image from the Docker hub
FROM apache/airflow:2.3.0-python3.8

# Install required Python packages
RUN pip install --no-cache-dir \
    apache-airflow-providers-kafka \
    apache-airflow-providers-flink \
    apache-airflow-providers-google \
    pandas \
    kafka-python \
    google-cloud-bigquery \
    dbt

# Set Airflow environment variables
ENV AIRFLOW_HOME=/opt/airflow

# Expose the necessary ports for the Airflow web server and scheduler
EXPOSE 8080

# Start the Airflow web server and scheduler
CMD ["bash", "-c", "airflow db init && airflow webserver & airflow scheduler"]
