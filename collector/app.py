from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from datetime import datetime

app = FastAPI()

def conn():
    return psycopg2.connect(host="postgres-service", database="sensordb",
                            user="postgres", password="password")

class Data(BaseModel):
    device_id: str
    temperature: float
    humidity: float

@app.post("/data")
def recv(d: Data):
    c = conn()
    cur = c.cursor()
    cur.execute("INSERT INTO sensor_data (device_id, temperature, humidity, timestamp) VALUES (%s,%s,%s,%s)",
                (d.device_id, d.temperature, d.humidity, datetime.now()))
    c.commit()
    cur.close(); c.close()
    return {"ok": True}

@app.get("/latest")
def latest():
    c = conn(); cur = c.cursor()
    cur.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()
    cur.close(); c.close()
    return {"latest": row}

@app.get("/health")
def health(): return {"status": "running"}