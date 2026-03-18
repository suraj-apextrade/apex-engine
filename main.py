from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# App se aane wala data
class TradeData(BaseModel):
    api_key: str
    secret_key: str
    exchange: str
    leverage: int

# Server check karne ka rasta
@app.get("/")
def read_root():
    return {"status": "Apex Trade Engine is LIVE and Running!"}

# Asli Trade lagane ka rasta
@app.post("/trade")
def execute_trade(data: TradeData):
    # Yahan baad mein hum Delta ka asli code lagayenge
    print(f"🚀 Signal Received! Exchange: {data.exchange}, Leverage: {data.leverage}x")
    return {"message": f"Successfully connected to {data.exchange} and trade initiated!"}
