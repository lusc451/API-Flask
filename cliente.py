import requests

response = requests.get("http://127.0.0.1:5000/empregados/cargo/analista")

print(response.text)