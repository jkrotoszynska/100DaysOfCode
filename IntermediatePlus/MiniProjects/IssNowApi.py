import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

#print(response) #<Response [200]>
#response.raise_for_status()

data = response.json()
print(data)

msg = response.json()["message"]
print(msg)