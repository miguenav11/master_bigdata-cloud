import requests

response = requests.get("https://rickandmortyapi.com/api/character/2")
data = response.json()

print(f"Name: {data["name"]}, Status: {data["status"]}")