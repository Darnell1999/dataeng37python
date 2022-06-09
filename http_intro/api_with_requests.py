import requests
import json
from pprint import pprint
#
# pc_req = requests.get("https://api.postcodes.io/postcodes/IG1 2UT")
#
# print(pc_req, type(pc_req))
#
# if pc_req.status_code == 200:
#     # print(dict(pc_req.headers))
#     # print(pc_req.headers, type(pc_req.headers))
#     pprint(type(pc_req.content))
#     print(pc_req.content)
#     postcode = pc_req.json()
#     print(type(postcode))
#     print(postcode['result']['nuts'])
#     print(postcode["result"]['eastings'], postcode["result"]["northings"])

# headers = {'Content-Type': 'application/json'}
# body = {'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]}
#
# pc_req = requests.post(
#     url="https://api.postcodes.io/postcodes",
#     headers=headers,
#     data=json.dumps(body)
# )
#
# if pc_req.status_code == 200:
#     pprint(pc_req.headers)
#     postcode = (json.loads(pc_req.content)
#     print(postcode['result']['admin_ward'])

# admin ward, easting, northings nuts code