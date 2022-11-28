from pymongo import MongoClient

client = MongoClient('mongodb+srv://Coba-1:c-1@cluster0.5tmyqsq.mongodb.net/?retryWrites=true&w=majority')

db = client.dbfirdaus

doc = {
    'name' : 'daus',
    'age' : 17
}

db.users.insert_one(doc)