import pymongo

client = pymongo.MongoClient()
# print(client)
#
db = client["starwars"]
# print(db)

# luke = db.characters.find_one({"name": "Luke Skywalker"})
# print(luke)
# print(luke["height"])

# droids = db.characters.find(
#     {"species.name": "Droid"}
# )
# for droid in droids:
#     print(droid.get("name"))

# dv = db.characters.find_one({"name": "Darth Vader"})
# print(dv["name"], dv["height"])
#
# yl = db.characters.find({"eye_color": "yellow"})
# for name in yl:
#     print(name.get("name"))

# male = db.characters.find({"gender": "male"})
# count = 0
# for m in male:
#     print(m["name"])
#     count += 1
#     if count == 3:
#         break

# home = db.characters.find({"homeworld.name": "Alderaan", "species.name": "Human"})
# for name in home:
#     print(name["name"])

import requests


# http_req = requests.get("https://swapi.dev/api/starships/10")
http_req13 = requests.get("https://swapi.dev/api/starships/13")
http_req14 = requests.get("https://swapi.dev/api/starships/14")
http_req25 = requests.get("https://swapi.dev/api/starships/15")
http_req31 = requests.get("https://swapi.dev/api/starships/31")
print(http_req25.content)
