import sqlite3

empregados = [
                {'nome': 'Valentina', 'cargo': 'Analista', 'salario':5000},
                {'nome': 'Lucas', 'cargo': 'Desenvolvedor', 'salario':6000},
                {'nome': 'Enzo', 'cargo': 'Analista', 'salario':4000},
             ]

conn = sqlite3.connect('enterprise.db')

cursor = conn.cursor()

for empregado in empregados:
    cursor.execute("""
                   INSERT INTO empregados (nome, cargo, salario)
                   VALUES (?, ?, ?)
                   """, (empregado['nome'], empregado['cargo'], empregado['salario']))

print("Dados inseridos com sucesso!")

conn.commit()
conn.close()