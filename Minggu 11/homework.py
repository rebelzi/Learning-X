from pymongo import MongoClient

client = MongoClient('mongodb+srv://Coba-1:c-1@cluster0.5tmyqsq.mongodb.net/?retryWrites=true&w=majority')

db = client.dbfirdaus

# Menambah Buku
db.books.insert_one({
    'title' : 'Harry Potter',
    'author' : 'J.K. Rowling',
    'rating' : '90'
})
db.books.insert_one({
    'title' : 'The Fisherman and the Fish',
    'author' : 'Joseph Choi',
    'rating' : '10'
})
db.books.insert_one({
    'title' : 'Fire in the Water',
    'author' : 'Some Dude',
    'rating' : '57'
})

# Mengupdate author buku
db.books.update_one(
    {'title' : 'The Fisherman and the Fish'},
    {'$set': {'author' : 'Jimmy Kim'}}
)

# Menghapus yang ratingnya 90
db.books.delete_one({'rating' : 90})



