🌩️ Cloud-Native Real-Time Sensor Analytics Pipeline

FastAPI • Kubernetes • Docker • PostgreSQL • Grafana • GCP

A production-grade cloud-native IoT pipeline that streams real-time temperature & humidity data, stores it reliably, and visualizes it using Grafana — deployed on a multi-node Kubernetes cluster on Google Cloud Platform (GCP).

🚀 Overview

This project implements an end-to-end cloud-native architecture using:

Microservices (Producer + Collector)

Docker containers

Kubernetes orchestration

PVC-backed PostgreSQL storage

Grafana-based real-time dashboards

The goal is to build a scalable, fault-tolerant sensor analytics system.

✨ Features
🔹 Real-Time Sensor Data

Producer generates live temperature & humidity data every 5 seconds

Collector API validates and stores readings in PostgreSQL

🔹 Containerized Microservices

Independent Producer and Collector microservices

Dockerized and pushed to DockerHub

🔹 Kubernetes Orchestration

Deployments manage rolling updates & scaling

Services (ClusterIP + NodePort) provide stable networking

PVC ensures no data loss

Automatic restart & pod recovery

🔹 Live Visualization

Grafana dashboard auto-refreshes

SQL-based visualizations in real time

📁 Project Structure
cloud-native-sensor-analytics-pipeline/
├── producer/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── collector/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── k8s/
│   ├── postgres.yaml
│   ├── collector.yaml
│   └── producer.yaml
└── README.md

⚙️ How to Run
1️⃣ Build & Push Docker Images
docker build -t <user>/producer ./producer
docker push <user>/producer

docker build -t <user>/collector ./collector
docker push <user>/collector

2️⃣ Deploy Kubernetes Resources
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/collector.yaml
kubectl apply -f k8s/producer.yaml

3️⃣ Verify Deployment
kubectl get pods -o wide
kubectl get svc
kubectl logs -l app=producer -f
kubectl logs -l app=collector -

4️⃣ Access Services
Service	Endpoint
Collector Latest Data	http://<NODE_IP>:31111/latest
Grafana Dashboard	http://<MASTER_IP>:3000

📊 Sample JSON Output
{
  "device_id": "sensor-01",
  "temperature": 28.66,
  "humidity": 38.86,
  "timestamp": "2025-11-29T00:19:30Z"
}

🌱 Future Enhancements
Integrate Kafka for high-throughput ingestion
Add Prometheus monitoring + Grafana alert rules
Deploy Grafana inside Kubernetes
Autoscale using HPA (Horizontal Pod Autoscaler)

🧑‍💻 Authors

Shreya Galurgi