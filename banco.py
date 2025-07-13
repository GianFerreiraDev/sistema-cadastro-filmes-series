import sqlite3

# Funções do banco de dados
def conectar_banco():
    # Função para conectar e garantir que as tabelas existam no banco 
    conexao = sqlite3.connect("filmes_series.db")
    cursor = conexao.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS titulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            ano INTEGER NOT NULL
        );
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
    # Função para listar todos os titulos do banco
    cursor.execute("SELECT id, nome, tipo, ano FROM titulos")
    return cursor.fetchall()
    
    
def atualizar_titulo(cursor, conexao, id, novo_nome=None, novo_tipo=None, novo_ano=None):
    # Função para atualizar os titulos do banco
    campos = []
    valores = []
    
    if novo_nome:
        campos.append("nome = ?")
        valores.append(novo_nome)
    if novo_tipo:
        campos.append("tipo = ?")
        valores.append(novo_tipo)
    if novo_ano:
        campos.append("ano = ?")
        valores.append(novo_ano)
        
    if not campos:
        return False


    valores.append(id)
    sql = f"UPDATE titulos SET {', '.join(campos)} WHERE id = ?"
    cursor.execute(sql, valores)
    conexao.commit()
    return True


def remover_titulo(cursor, conexao, id):
    # Função para remover titulos do banco
    cursor.execute("DELETE FROM titulos WHERE id = ?", (id,))
    conexao.commit()
    return cursor.rowcount > 0
