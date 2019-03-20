AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
print(AFC_east[2][6:])
for team in AFC_east:
    print(team)

AFC_west = ['Chargers', 'Raiders','Broncos','Chiefs']
AFC = AFC_east + AFC_west
print(AFC)

# Dictionary

names = ['B', 'M','A']
score = [60,90,100]
grades = {}
grades[names[0]]=score[0]
grades[names[1]]=score[1]
grades[names[2]]=score[2]
print(grades)
print( 'A' in grades)
for name in grades.keys():
    print(name)
for score in grades.values():
    print(score)
for grade in grades.items():
    print(grade)

# json_example
import urllib.request
import json

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
city = 'Wellesley'
country_code = 'us'
url = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'.format(
    city=city, country_code=country_code, APIKEY=APIKEY)

print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)

# How do we get current temperature?
import pprint
pprint.pprint(response_data)
print(response_data['main']['temp']-273.15)

import mbta_helper
print(mbta_helper.find_stop_near('Newton'))
