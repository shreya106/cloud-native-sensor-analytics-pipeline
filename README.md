# Cloud-Native Sensor Analytics Pipeline

A real-time IoT analytics pipeline deployed on Kubernetes.

## Features
- FastAPI Producer → sends sensor data every 5s
- FastAPI Collector → stores to PostgreSQL
- PVC-backed database for durability
- Grafana visual dashboard
- Kubernetes orchestration (Deployments, Services, PVC)

## Run
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/collector.yaml
kubectl apply -f k8s/producer.yaml
