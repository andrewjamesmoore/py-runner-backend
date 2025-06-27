import os
from pymongo import MongoClient
from methods import METHODS
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"))

db = client["py_runner_data"]
collection = db["methods"]

collection.delete_many({})
print("Existing documents cleared.")

collection.insert_many(METHODS)
print(f"Inserted {collection.count_documents({})} documents.")

