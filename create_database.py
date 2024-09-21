import sqlite3

conn = sqlite3.connect('enterprise.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE empregados(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   cargo TEXT,
                   salario REAL
               );
""")

print("Banco criado com sucesso!")

# Encerrando a conexão com o banco de dados
conn.close()