import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.billboard.com/charts/hot-100/',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('.o-chart-results-list-row')

for song in songs:
    song_rating = song.select_one('.o-chart-results-list__item > .a-font-primary-bold-l').text.strip()
    song_info = song.select_one('.o-chart-results-list__item > h3')
    song_title = song_info.text.strip()
    song_singer = song_info.parent.select_one('span').text.strip()
    print(song_rating, '/' ,song_title, '/', song_singer)
