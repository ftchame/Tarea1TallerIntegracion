import json
import pprint
import hashlib

with open("prueba") as json_file:
    json_data = json.load(json_file)
    print(json_data)

for item in json_data:

prueba = hashlib.sha256("").hexdigest()
print(prueba)