import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('mongodb+srv://Coba-1:c-1@cluster0.5tmyqsq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbfirdaus

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('.lister > table > tbody > tr')

for movie in movies:
    movie_title = movie.select_one('.titleColumn > a').text
    movie_year = movie.select_one('.titleColumn > span').text
    movie_year = movie_year.replace('(','')
    movie_year = movie_year.replace(')','')
    movie_rating = movie.select_one('.ratingColumn > strong').text
    doc = {
        'movie' : movie_title,
        'year' : movie_year,
        'rating' : movie_rating 
    }
    db.movies.insert_one(doc)
    