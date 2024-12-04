import requests
import json

response = requests.get("https://httpbin.org/get")
print("Código da resposta: ", response.status_code)
print("Resposta: ", json.dumps(response.json()))

data = ""