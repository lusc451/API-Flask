import requests

response = requests.get("http://127.0.0.1:5000/empregados/cargo/analista")

message = response.json()
print(message['empregados'])