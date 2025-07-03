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
