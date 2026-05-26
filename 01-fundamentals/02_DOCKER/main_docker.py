import requests
import numpy as np

arr = np.array([1, 2, 3])
print(arr)

response = requests.get("https://catfact.ninja/fact")
print(response)
data = response.json()
print(data)
