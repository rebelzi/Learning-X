import requests # Membutuhkan instalasi requests library

r = requests.get('http://spartacodingclub.shop/en/global_air/seoul')
rjson = r.json()

days = rjson['data']['forecast']

for day in days:
    if day['avg'] < 60:
        print(day['day'], day['avg'])