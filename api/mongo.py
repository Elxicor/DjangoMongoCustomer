from pymongo import MongoClient

MONGO_URI = "mongodb+srv://oop:oop@cluster0.9knxc.mongodb.net/?appName=Cluster0"

DB_NAME = "oop"         
COLLECTION = "Customers"  

def get_collection():
    client = MongoClient(MONGO_URI)  
    db = client[DB_NAME]
    return db[COLLECTION]
