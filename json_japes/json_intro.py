import json

# car_data = {
#
#     "make": "Tesla",
#     "type": "Electric",
#     "faults": 9384,
#     "death_trap": True,
#     "driver": None
# }
#
# dumps = json.dumps(car_data)
#
# print(dumps, type(dumps))
#
# with open('tesla.json', 'w') as jsonfile:
#     json.dump(car_data, jsonfile)
#

with open("tesla.json") as jsonfile:
    tesla = json.load(jsonfile)

print(tesla, type(tesla))
