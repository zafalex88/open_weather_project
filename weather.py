import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"
city = input('Enter a city name to view its weather: ')

querystring = {"callback":"test","id":"2172797","lang":"-en","metric":"units","q":city}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "78034bcf5emsh6d33f4776102e77p10adaajsn7041714f6122"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
input()