import requests
import json

url = 'http://api.openweathermap.org/data/2.5/weather?id=2023469&appid=d6843ab8ee963f5d372296dfff62aed7'
response = requests.get(url)
data = json.loads(response.text)
print(data)