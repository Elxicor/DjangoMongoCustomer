from django.http import JsonResponse
from .mongo import get_collection
from pymongo import MongoClient

def customers(request):
    col = get_collection()

    docs = list(col.find({}, {"_id": 0}))  

    return JsonResponse({"data": docs}, safe=True)

def mongo_info(request):
    from .mongo import MONGO_URI
    client = MongoClient(MONGO_URI)  
    dbs = client.list_database_names()
    return JsonResponse({"databases": dbs})
