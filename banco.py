#importando SQLite
import sqlite3 as lite

#Criando conexao
con = lite.connect('dados.db')

#Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT ,telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")


#
