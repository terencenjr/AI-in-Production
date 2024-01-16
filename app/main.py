from phi2 import respond
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": respond("What is AI?")}