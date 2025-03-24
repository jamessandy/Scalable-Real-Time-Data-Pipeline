# Real-Time Data Pipeline for E-commerce Business

## Project Overview
An e-commerce business needs to be capture real-time user behavior and transactional data to be able help in personalization, marketing optmization and fraud detection. This Solution is a scalable real-time data pipeline that collects, processe and stores behabior data from diffrent sources and deliver insights for instant decison maing. 

## Architecture




## **Technologies Used**

- **Kafka** (Real-time Data Ingestion)
- **Apache Flink** (Stream Processing)
- **Apache Airflow** (Workflow Orchestration)
- **Google BigQuery** (Data Storage & Analytics)
- **DBT** (Data Transformation)
- **Looker** (Data Visualization)

# **How to Run This Project**

## **Installation & Setup**

### **Step 1: Clone the Repository**

Clone the repository to your local machine:

```bash
git clone   
cd 
```

### **Step 2: Install Dependencies**

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### **Step 3: Set Up Kafka**

Set up Apache Kafka locally or use a cloud-based Kafka service.\
If running locally, start **Zookeeper** and **Kafka**:

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties &  
bin/kafka-server-start.sh config/server.properties
```

Create Kafka topics:

```bash
bin/kafka-topics.sh --create --topic ecommerce_transactions --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3
```

### **Step 4: Docker Setup**

To deploy the entire system using Docker, build and start the containers:

```bash
docker-compose up --build
```

This starts Kafka, Flink, Airflow, and all required services.

---

## **Running the Project**

### **1. Start the Kafka Pipeline**

- **Run Kafka Producer** (Simulates real-time transactions):
  ```bash
  python kafka_producer.py
  ```
- **Run Kafka Consumer** (Processes and streams data to Flink):
  ```bash
  python kafka_consumer.py
  ```

### **2. Run Flink Job (Real-time Processing)**

Start the Flink job to process transaction data:

```bash
python flink_processing.py
```

### **3. Execute Airflow DAG (Batch Processing)**

Trigger the Airflow DAG for batch processing:

```bash
airflow dags trigger ecommerce_batch_processing
```

### **4. Run DBT for Data Transformation**

```bash
dbt run --profiles-dir bigquery/dbt
```

### **5. Visualize in BigQuery / Power BI**

Once data is processed and stored in **Google BigQuery**, connect Power BI or Tableau for visualization.
