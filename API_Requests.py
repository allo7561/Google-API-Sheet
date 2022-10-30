import requests

req = requests.get(url='http://localhost:5000/api/activity/J')

print(req.json()[0])