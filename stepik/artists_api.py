import requests
import json

client_id = "52876c72f3f1228e6486"
client_secret = "600fe1021aa9273c914dee21e554067e"

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера и достаем токен
j = json.loads(r.text)
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

url = "https://api.artsy.net/api/artists/"
artists = {}

with open("in.txt", encoding="utf-8") as f:
    for line in f:
        url_api = url + line.strip()
        r = requests.get(url_api, headers=headers)
        j = json.loads(r.text)
        artists[j["sortable_name"]] = j["birthday"]

for artist in sorted(artists.items(),  key=lambda x: (x[1], x[0])):
    print(artist[0])
