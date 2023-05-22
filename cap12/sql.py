import sqlite3

con = sqlite3.connect("pytohn/Cursodsa/cap12/cap12_dsa.db")
cursor = con.cursor()

sqlquery = "SELECT name FROM sqlite_master WHERE type = 'table';"

# cursor.execute(sqlquery)


sqlquery = "SELECT * FROM tb_vendas_dsa;"

# cursor.execute(sqlquery)


sqlquery = "SELECT nome_produto, AVG(unidades_vendidas) FROM tb_vendas_dsa GROUP BY nome_produto;"

cursor.execute(sqlquery)

print(cursor.fetchall())

cursor.close()
con.close()
