import json
import  requests

URL = "http://127.0.0.1:8000/stucreate/"

# For Posting some data
data = {
    'name': 'Mission',
    'roll': 101,
    'city': 'Delhi'
}

json_data = json.dumps(data)
r=requests.post(url=URL,data=json_data)
new_data=r.json()
print(new_data)

# import json
# import requests

# URL = "http://127.0.0.1:8000/stucreate/"

# data = {
#     'name': 'Mission',
#     'roll': 101,
#     'city': 'Delhi'
# }

# json_data = json.dumps(data)
# headers = {'Content-Type': 'application/json'}
# r = requests.post(url=URL, data=json_data, headers=headers)

# try:
#     new_data = r.json()
#     print(new_data)
# except json.JSONDecodeError:
#     print("Response is not in JSON format")
#     print(r.text)