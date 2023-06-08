
import uvicorn
from fastapi import FastAPI
import os

# initialize FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"data": "Application ran successfully - FastAPI"}