import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()

pos = data["iss_position"]

lat = pos["latitude"]
lon = pos["longitude"]

print(lat)
print(lon)
#added
