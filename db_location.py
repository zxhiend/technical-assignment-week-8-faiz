from typing import Collection
import pymongo
import uuid

client = pymongo.MongoClient("mongodb+srv://s2wneamsi:kelompok8@cluster0.tsgsyfp.mongodb.net/?retryWrites=true&w=majority")
db = client.Location
collection = db.llokasi

def locationn(kecepatan,latitude,longitude,timestamp):
    data = {
        "ID transaksi": str(uuid.uuid4()),
        "kecepatan": kecepatan,
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp
    }
    records = collection.insert_one(data)
    print("data tersimpan",records)

