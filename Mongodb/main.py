import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["learn"]
collection = db["learningMongo"]

data1 = {
    "name": "Ismael",
    "age": 16,
    "position": "Developer",
}

data2 = {
    "name": "Pirolise",
    "age": 26,
    "position": "Developer",
}

data3 = {
    "name": "Eduarda",
    "age": 17,
    "position": "Developer",
}

allData = [data1, data2, data3]

for i in allData:
    collection.insert_one(i)

result = collection.find_one({"name": "Ismael"})
print(result)

results = collection.find({"age": {"$gte": 17}})

for x in results:
    print(x)

