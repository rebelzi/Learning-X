from pymongo import MongoClient

client = MongoClient('mongodb+srv://Coba-1:c-1@cluster0.5tmyqsq.mongodb.net/?retryWrites=true&w=majority')

db = client.dbfirdaus

doc1 = {'name' : 'daus', 'age' : 17}
doc2 = {'name' : 'firdaus', 'age' : 19}
doc3 = {'name' : 'daus', 'age' : 20}

db.users.insert_one(doc1)
db.users.insert_one(doc2)
db.users.insert_one(doc3)