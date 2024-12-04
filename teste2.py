import requests
import json

data = {
    "nome": "Vinicius",
    "idade": 30,
}

response = requests.post("https://httpbin.org/post", data=data)
print("Código da resposta: ", response.status_code)
print("Resposta: ", json.dumps(response.json()))
