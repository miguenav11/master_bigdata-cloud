import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    data = response.json()
    print(data)
except:
    print("Ha ocurrido un error")
