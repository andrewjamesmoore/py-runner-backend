from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .functions import BUILTIN_FUNCTIONS
import json
from pathlib import Path

app = FastAPI()

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

@app.get("/functions", response_model=List[PythonFunction], tags=["Functions"])
def get_functions():
    return BUILTIN_FUNCTIONS