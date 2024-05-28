import sqlite3 as lite

# Conectando ao db
con = lite.connect('dados.db')

# Inserir dados
def inserir_dados(dados):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data, valor, serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, dados)

# Atualizar dados
def atualizar_dados(dados):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data=?, valor=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, dados)

# Deletar dados
def deletar_dados(id):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query, id)

# Ver todos os dados
def ver_todos_dados():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        # Pega todas as linhas da tabela
        rows = cur.fetchall()
        # Para cada linha, adiciona a linha à lista de dados
        for row in rows:
            ver_dados.append(row)
    return ver_dados


# Ver dados individuais
def ver_dados_individuais(id):
    ver_dados_individuais = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individuais.append(row)
    return ver_dados_individuais
