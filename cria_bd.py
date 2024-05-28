import sqlite3 as lite

# Criando conexão
con = lite.connect("dados.db")

# Criando tabela
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data DATE, valor DECIMAL, serie TEXT, imagem TEXT)")
