from tiny_llama import respond
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": respond("What is AI?")}

@app.get("/health")
async def health():
    return "200 OK"