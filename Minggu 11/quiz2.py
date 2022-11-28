from pymongo import MongoClient
client = MongoClient('mongodb+srv://Coba-1:c-1@cluster0.5tmyqsq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbfirdaus


# target_film = db.movies.find_one({'movie':'Goodfellas'}) (mentarget judul film yang mau dilihat ratingnya)
# print(target_film['rating']) (memunculkan rating sesuai judul di target_film)

# target_rating = target_film['rating']
# movies = list(db.movies.find({'rating': target_rating}))
# for movie in movies:
    # print(movie['movie'])
# code diatas untuk memunculkan judul film yang ratingnya sama yang ditargetkan di target_film

db.movies.update_one(
    {'movie': 'Goodfellas'},
    {'$set': {'rating': '0'}}
)


