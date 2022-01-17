#python 2
import json
import csv
import urllib
import io

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
data = urllib.urlopen(url).read()
jsonData = json.loads(data)
attractionsList = jsonData['result']['results']
with io.open("data.csv", "w", encoding="utf-8") as file:
    for attraction in attractionsList:
        district = attraction['address'][5:8]
        firstImageUrl = attraction['file'].lower().split('jpg')[0]+'jpg'
        file.write(attraction['stitle']+","+district+','+attraction['longitude']+','+attraction['latitude']+','+firstImageUrl+"\n")


