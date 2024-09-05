
# This is third party app that will be used to make requests to the GS1 API
import requests

URL="http://127.0.0.1:8000/stuinfo/"

r=requests.get(url=URL)

data=r.json()

print(data)