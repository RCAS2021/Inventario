import sqlite3 as lite

# Conectando ao db
con = lite.connect('dados.db')

dados = ['vaso', 'sala', 'vaso teste', 'vasomarca', '27052024', '25.99', 'series', 'local_imagem.png']
# Inserir dados
with con:
    cur = con.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data, valor, serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(query, dados)

atualizar_dados = ['sofa', 'sala', 'sofa teste', 'sofamarca', '27052024', '27.99', 'series', 'local_imagem.png', 1]
# Atualizar dados
with con:
    cur = con.cursor()
    query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data=?, valor=?, serie=?, imagem=? WHERE id=?"
    cur.execute(query, atualizar_dados)

# Ver dados
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

print(ver_dados)