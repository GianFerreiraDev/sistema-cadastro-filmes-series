import sqlite3

# Funções do banco de dados
def conectar_banco():
    # Função para conectar e garantir que a tabela existe no banco 
    conexao = sqlite3.connect("filmes_series.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS titulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            ano INTEGER NOT NULL
        )
    """)
    conexao.commit()
    return conexao, cursor


def inserir_titulo(conexao, cursor, nome, tipo, ano):
    # Função para inserir novos titulos ao banco
    cursor.execute("""
        INSERT INTO titulos (nome, tipo, ano)
        VALUES (?, ?, ?)
    """,  (nome, tipo, ano))
    conexao.commit()


def buscar_todos_titulos(cursor):
    cursor.execute("SELECT id, nome, tipo, ano FROM titulos")
    return cursor.fetchall()
