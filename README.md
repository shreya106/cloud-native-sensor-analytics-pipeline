🌩️ Cloud-Native Real-Time Sensor Analytics Pipeline

FastAPI • Kubernetes • Docker • PostgreSQL • Grafana • GCP

A production-grade cloud-native IoT pipeline that streams real-time temperature & humidity data, stores it reliably, and visualizes it using Grafana — all deployed on a multi-node Kubernetes cluster on Google Cloud Platform (GCP).

🚀 Overview

This project demonstrates a complete cloud-native microservices architecture:

Producer microservice simulates live sensor readings every 5 seconds

Collector microservice validates & stores data into PostgreSQL

PostgreSQL persists data using a Kubernetes PVC

Grafana visualizes real-time trends

Kubernetes manages deployments, networking, auto-healing, and scaling

🧩 Architecture
 ┌────────────┐     JSON      ┌─────────────┐     SQL Inserts     ┌─────────────┐      SQL Queries      ┌─────────────┐
 │ PRODUCER   │ ────────────► │ COLLECTOR   │ ───────────────────► │ POSTGRESQL  │ ─────────────────────► │  GRAFANA    │
 │ (FastAPI)  │               │ (FastAPI)   │                      │ (PVC-backed)│                        │ Dashboard UI│
 └────────────┘               └─────────────┘                      └─────────────┘                        └─────────────┘


✔ Real-time → ingestion → database → live dashboard
✔ Stateless microservices + persistent storage
✔ Kubernetes handles pod scheduling, service discovery & recovery

✨ Features
🔹 Real-Time Sensor Data

Producer generates temperature + humidity readings every 5 seconds

Collector API stores readings in PostgreSQL

🔹 Containerized Microservices

Dockerized Producer + Collector

Images pushed to DockerHub

🔹 Kubernetes Orchestration

Deployments for Producer, Collector, PostgreSQL

Services (ClusterIP + NodePort) ensure stable networking

PVC prevents data loss even if pods restart

Auto-healing + multi-node scheduling on GCP

🔹 Live Visualization

Grafana dashboards with auto-refresh

SQL queries visualize database values in real time

📁 Project Structure
cloud_project/
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
│   ├── producer.yaml
│   └── collector.yaml
└── README.md

⚙️ How to Run
1️⃣ Build & Push Docker Images
docker build -t <user>/producer ./producer
docker push <user>/producer

docker build -t <user>/collector ./collector
docker push <user>/collector

2️⃣ Apply Kubernetes Manifests
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/collector.yaml
kubectl apply -f k8s/producer.yaml

3️⃣ Verify Deployment
kubectl get pods -o wide
kubectl get svc
kubectl logs -l app=producer -f
kubectl logs -l app=collector -f

4️⃣ Access Services
Service	URL
Collector API (latest)	http://<NODE_IP>:31111/latest
Grafana Dashboard	http://<MASTER_IP>:3000
📊 Sample Output (Producer → Collector → PostgreSQL)
{
  "device_id": "sensor-01",
  "temperature": 28.66,
  "humidity": 38.86,
  "timestamp": "2025-11-29T00:19:30Z"
}

🌱 Future Enhancements

Add Kafka for high-throughput streaming

Add Prometheus + Grafana Alerts

Deploy Grafana inside Kubernetes

Scale replicas based on load

🧑‍💻 Authors

Shreya Galurgi