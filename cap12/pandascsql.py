import sqlite3

import pandas as pd

con = sqlite3.connect("pytohn/Cursodsa/cap12/cap12_dsa.db")
cursor = con.cursor()

sqlquery = "SELECT * FROM tb_vendas_dsa;"
cursor.execute(sqlquery)

dados = cursor.fetchall()

df = pd.DataFrame(dados, columns=["Id_Pedido",
                                  "Id_Produto",
                                  "Nome_Produto",
                                  "Valor_Unitario",
                                  "Unidades_Vendidas",
                                  'Custo'])

media_unidades = df.groupby("Nome_Produto")['Unidades_Vendidas'].mean()
print(media_unidades.head(10))

cursor.close()
con.close()
