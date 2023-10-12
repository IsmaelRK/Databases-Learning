import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["learn"]
collection = db["learningMongo"]

collection.update_one({"name": "Pirolise"}, {"$set": {"idade": 35}})
