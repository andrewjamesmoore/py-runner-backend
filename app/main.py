from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path

load_dotenv()

app = FastAPI()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["py_runner_data"]

class PythonFunction(BaseModel):
    name: str
    description: str
    example: str

@app.get("/")
def root():
    return {"Message: API is up and running!"}

@app.get("/examples")
def get_examples():
    data_path = Path(__file__).parent / "data.json"
    with open(data_path) as f:
        return json.load(f)

@app.get("/functions")
def get_functions():
    return list(db["builtin_functions"].find({}, {"_id": 0}))

@app.get("/methods")
def get_methods():
    return list(db["methods"].find({}, {"_id": 0}))
