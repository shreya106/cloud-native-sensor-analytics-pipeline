from fastapi import FastAPI
import requests, random, threading, time

COLLECTOR_URL = "http://collector-service:8001/data"
app = FastAPI()

def send_data():
    while True:
        payload = {
            "device_id": "sensor-01",
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(30, 60), 2)
        }
        try:
            requests.post(COLLECTOR_URL, json=payload)
        except:
            pass
        time.sleep(5)

@app.on_event("startup")
def start():
    threading.Thread(target=send_data, daemon=True).start()

@app.get("/health")
def health():
    return {"status": "running"}