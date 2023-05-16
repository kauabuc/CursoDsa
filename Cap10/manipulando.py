import pandas as pd

dsa_df = pd.read_csv('pytohn/Cursodsa/Cap10/dataset.csv')


moda = dsa_df['Quantidade'].value_counts().index[0]
dsa_df['Quantidade'].fillna(value=moda, inplace=True)
# print(dsa_df.head(5))

df3 = dsa_df.query("229 < Valor_Venda < 10000")
# print(df3.describe())

df4 = dsa_df.query("766 < Valor_Venda")
# print(df4.describe())


# print(dsa_df[dsa_df['Quantidade'].isin([5, 7, 9, 11])][:10])

ds2 = dsa_df[(dsa_df.Segmento == 'Home Office') &
             (dsa_df.Regiao == 'South')].head()
ds3 = dsa_df[(dsa_df.Segmento == 'Home Office') |
             (dsa_df.Regiao == 'South')].tail()
ds4 = dsa_df[(dsa_df.Segmento != 'Home Office') &
             (dsa_df.Regiao != 'South')].sample(5)

# print(ds2)
# print(ds3)
# print(ds4)


ds5 = dsa_df[["Segmento", "Regiao", "Valor_Venda"]
             ].groupby(["Segmento", "Regiao"]).mean()
# print(ds5)


ds6 = dsa_df[["Segmento", "Regiao", "Valor_Venda"]
             ].groupby(["Segmento", "Regiao"]).agg(["mean", "count", "std"])
print(ds6)

# Pesquisar dados
dsa_df[dsa_df.Segmento.str.endswith("mer")].head()


dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split("-").str[1]
print(dsa_df.head())
