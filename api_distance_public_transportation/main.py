from functions import distance
from fastapi import FastAPI
from models import Payload

app = FastAPI()

@app.post("/")
async def model_predict_etr(payload: Payload) -> dict:
    dist = await distance(payload)    
    return dist