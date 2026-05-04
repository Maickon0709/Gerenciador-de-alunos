import sqlite3

def conectar():
    conexao = sqlite3.connect("MeuBanco.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            plano TEXT
        )
    """)
    conexao.commit()
    
    return conexao, cursor