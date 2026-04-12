import sqlite3

def conectar():
    conexao = sqlite3.connect("MeuBanco.db")
    cursor = conexao.cursor()
    return conexao, cursor