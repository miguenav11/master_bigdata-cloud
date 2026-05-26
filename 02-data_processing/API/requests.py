import requests

# 1. Definir la URL
url = "https://api.ejemplo.com/datos"

# 2. Hacer la petición GET
response = requests.get(url)

# 3. Comprobar si salió bien
if response.status_code == 200:
    data = response.json()  # Convertimos la respuesta a un diccionario/lista de Python
    print(data)
else:
    print(f"Error: {response.status_code}")