from api_distance_public_transportation.functions import distance
from api_distance_public_transportation.models import Payload
from fastapi import FastAPI


app = FastAPI()

@app.post("/")
async def my_distance(payload: Payload) -> dict:
    dist = await distance(payload)    
    return dist