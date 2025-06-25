from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

@app.get("/")
def root():
    return {"Message: API is up and running!"}

@app.get("/examples")
def get_examples():
    data_path = Path(__file__).parent / "data.json"
    with open(data_path) as f:
        return json.load(f)