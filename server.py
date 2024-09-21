from flask import Flask

app = Flask(__name__)

empregados = [
                {'nome': 'Valentina', 'cargo': 'Analista', 'salario':5000},
                {'nome': 'Lucas', 'cargo': 'Desenvolvedor', 'salario':6000},
                {'nome': 'Enzo', 'cargo': 'Analista', 'salario':4000},
             ]

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/empregados")
def get_empregados():
    return {'empregados': empregados}

@app.route("/empregados/<cargo>")
def get_empregados_cargo(cargo):
    
    out_empregados = []
    for empregado in empregados:
        if cargo == empregado['cargo']:
            out_empregados.append(empregado)
    
    return out_empregados
    

if __name__ == "__main__":
    app.run(debug=True)
    