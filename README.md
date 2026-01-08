🌐 Cloud-Native Real-Time Sensor Analytics Pipeline

Real-time IoT data pipeline built using FastAPI, Docker, Kubernetes, PostgreSQL, and Grafana on Google Cloud Platform (GCP).
The system streams sensor readings every 5 seconds, stores them reliably, and visualizes them live.

🚀 Features

🔵 Real-Time Sensor Stream

Producer microservice sends temperature & humidity every 5 seconds

Collector validates the data & inserts into PostgreSQL

🔵 Cloud-Native Microservices

Python FastAPI microservices

Dockerized & deployed on Kubernetes

Auto-restart, scaling, and scheduling handled by Kubernetes

🔵 Persistent Storage

PostgreSQL with PVC-backed persistent volume

Ensures zero data loss during pod restarts

🔵 Stable Networking

ClusterIP for internal service-to-service communication

NodePort to expose Collector & Grafana to users

🔵 Live Visualization

Grafana dashboards with auto-refresh

SQL queries read real-time values from PostgreSQL

🧰 Tech Stack

Layer	Technology

Backend	FastAPI, Python

Database	PostgreSQL + PersistentVolumeClaim

Visualization	Grafana

Containerization	Docker, DockerHub

Orchestration	Kubernetes (Deployments, Services, PVC)

Networking	Flannel CNI

Cloud	Google Cloud Platform (GCP VMs)

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

3️⃣ Verify Everything is Running

kubectl get pods -o wide

kubectl get svc

kubectl logs -l app=producer -f

kubectl logs -l app=collector -f

4️⃣ Access Services

Service	URL

Collector /latest	http://<NODE_IP>:31111/latest

Grafana Dashboard	http://<MASTER_IP>:3000

📊 Sample Output (Producer → Collector → PostgreSQL)

{

    "device_id": "sensor-01",
    
    "temperature": 28.66,
    
    "humidity": 38.86,
    
    "timestamp": "2025-11-29T00:19:30Z"
    
}

🌱 Future Enhancements

Replace REST ingestion with Kafka for high-throughput streaming

Support multiple sensor types

Autoscaling with Kubernetes HPA

Deploy Grafana inside Kubernetes

**GRAFANA OUTPUT**

<img width="1411" height="789" alt="Grafana" src="https://github.com/user-attachments/assets/2e87e7e2-5336-4779-b0d1-cdfcb2dbe812" />



🧑‍💻 Author

Shreya Galurgi
