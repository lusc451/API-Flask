import requests

data = {"username": "Carlos", "secret": "@dmin456", "cargo":"Engenheiro", "nome":"Jose", "salario": "6500"}

response = requests.post("http://127.0.0.1:5000/register", data=data)

# response = requests.get('http://127.0.0.1:5000/empregados/salario/5000')

if response.status_code == 200:
    message = response.json()
    print(message['empregados'])
else:
    print(response.status_code)