from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["nips2024"]
collection = db["papers"]

collection.create_index([
    ("title", "text"),
    ("authors", "text")
])

print("Text index created!")
