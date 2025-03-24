# Use an official Flink image from the Docker hub
FROM apache/flink:1.13-scala_2.12

# Install additional dependencies if required
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install necessary Python packages for Flink (if using Python in your jobs)
RUN pip3 install kafka-python

# Set working directory for the Flink jobs
WORKDIR /opt/flink

# Copy the Flink job jar (this is the compiled jar for your Flink job)
COPY ./jobs/flink_job.jar /opt/flink

# Expose the necessary ports for Flink UI and job submission
EXPOSE 8081

# Start the Flink job cluster
CMD ["bin/start-cluster.sh"]
