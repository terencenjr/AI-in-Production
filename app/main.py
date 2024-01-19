from tiny_llama import respond
from request import Request
from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to Llama Chat!"

@app.post("/chat")
async def chat(request: Request):
    print(f"Prompt received: {request.prompt}")
    response = respond(request.prompt)
    return {"message": prettify(response)} 

def prettify(response: str):
    return re.sub("(\[\/INST]|\[\/SYS]|\\n)", "", response) # Remove all the tags and newlines