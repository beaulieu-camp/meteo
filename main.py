import json
import requests
import sys

token = sys.argv[-1]

lat = "48.1160682"
lon = "-1.6401422"

url = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+token+"&units=metric";
meteo = requests.get(url).json()

temperature = int(meteo["main"]["temp"])
code = meteo["weather"][0]["icon"]

with open("./out/index.json","w+") as file:
    file.write(json.dumps({"temperature":temperature,"code":code}))
