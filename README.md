🌩️ Cloud-Native Real-Time Sensor Analytics Pipeline

FastAPI • Kubernetes • Docker • PostgreSQL • Grafana • GCP

A real-time cloud-native IoT data pipeline designed to ingest, store, and visualize sensor readings using Kubernetes microservices, persistent storage, and Grafana dashboards.
Built on a multi-node Kubernetes cluster running on Google Cloud Platform (GCP).

🚀 Project Architecture
 ┌────────────┐     JSON      ┌───────────────┐     SQL       ┌──────────────┐     Visuals     ┌────────────┐
 │  PRODUCER   │ ───────────▶ │   COLLECTOR    │ ───────────▶ │  POSTGRESQL   │ ─────────────▶ │   GRAFANA   │
 │  (FastAPI)  │              │   (FastAPI)    │              │  (PVC-backed) │                │  Dashboard  │
 └────────────┘               └───────────────┘              └──────────────┘                └────────────┘


✔ Producer sends live temperature & humidity
✔ Collector validates + stores into PostgreSQL
✔ Grafana visualizes via live auto-refresh charts
✔ Kubernetes manages deployments, scaling, storage & recovery

🧩 Features
🔹 Real-Time Sensor Data

Producer microservice generates temperature & humidity data every 5 seconds

Automatic REST-based data ingestion

🔹 Containerized Microservices

Dockerized Producer & Collector

Images pushed to DockerHub

🔹 Kubernetes Orchestration

Deployments for Producer, Collector, PostgreSQL

Services (ClusterIP + NodePort) for stable networking

PVC-backed PostgreSQL ensures no data loss

Auto-healing pods & multi-node scheduling on GCP

🔹 Live Visualization

Grafana dashboards with auto-refresh

SQL queries visualize database values in real-time

📦 Tech Stack
Layer	Technology
Backend	FastAPI, Python
Database	PostgreSQL + PersistentVolumeClaim
Visualization	Grafana
Containerization	Docker, DockerHub
Orchestration	Kubernetes (Deployments, Services, PVC, PV)
Networking	Flannel CNI
Cloud Hosting	Google Cloud Platform (GCP VMs)
📁 Project Structure
cloud_project/
│
├── producer/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── collector/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── k8s/
│   ├── postgres.yaml
│   ├── producer.yaml
│   └── collector.yaml
│
└── README.md

⚙️ How to Run
1️⃣ Build & Push Docker Images
docker build -t <dockerhub>/producer ./producer
docker push <dockerhub>/producer

docker build -t <dockerhub>/collector ./collector
docker push <dockerhub>/collector

2️⃣ Apply Kubernetes Manifests
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/collector.yaml
kubectl apply -f k8s/producer.yaml

3️⃣ Verify
kubectl get pods -o wide
kubectl get svc
kubectl logs -l app=producer -f
kubectl logs -l app=collector -f

4️⃣ Access Services
Component	URL
Collector /latest	http://<NODE-IP>:31111/latest
Grafana Dashboard	http://<MASTER-IP>:3000
📊 Sample Output (Producer → Collector → PostgreSQL)
{
  "device_id": "sensor-01",
  "temperature": 28.66,
  "humidity": 38.86,
  "timestamp": "2025-11-29T00:19:33Z"
}

🏗️ Future Enhancements

Add Kafka for high-throughput event streaming

Add Prometheus for system metrics

Add Horizontal Pod Autoscaler (HPA)

Add support for multiple sensor types

Deploy Grafana inside Kubernetes instead of VM

👩‍💻 author
Name: Shreya Galurgi
