import requests
from pprint import pprint

print("Задача 1")
name_list = ["Hulk", "Captain America", "Thanos"]
for name in name_list:
    URL = f"https://superheroapi.com/api/2619421814940190/search/{name}"
    response = requests.get(URL).json()
    # pprint(response)
    intelligence = response["results"][0]["powerstats"]["intelligence"]
    hero_dict = {}
    hero_dict[name] = int(intelligence)
    # print(hero_dict)
max_count = 0
hero = None
for key, value in hero_dict.items():
    if max_count < value:
        max_count = value
        hero = key
    print(f'{key} - {value}')





