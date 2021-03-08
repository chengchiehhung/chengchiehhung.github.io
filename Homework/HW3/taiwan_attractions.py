import requests
import json
import re

response = requests.get('https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json')
response = response.json()

attractions = response['result']['results']
# print(attraction.keys()) # Used to check what information it provides
# What we need are the keys: 'stitle', 'longitude', 'latitude', 'file'

for attraction in attractions:
    # Getting info. we need
    site_title = attraction['stitle']
    longitude = attraction['longitude']
    latitude = attraction['latitude']
    photo_links = attraction['file']
  
    try:
        first_photo = photo_links[:photo_links.index('http://', 1)]
    except: # If file only has one photo
        first_photo = photo_links

    with open('data.txt', 'a+', encoding='UTF-8') as file:
        file.write(', '.join([site_title, longitude, latitude, first_photo]) + "\n")
