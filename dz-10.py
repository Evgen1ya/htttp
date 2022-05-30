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
print("Задача 2")

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    path_to_file = "netology/mytxt.txt"
    token = "token"
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(path_to_file, "mytxt.txt")





