import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["learn"]
collection = db["learningMongo"]

collection.delete_many({"position": "Developer"})  # _many ou _one | -> result.deleted_count
