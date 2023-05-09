import pandas as pd

arquivo = "pytohn/Cursodsa/Cap06/arquivos/salarios.csv"
df = pd.read_csv(arquivo)
print(df.head())
print(df["Position Title"].value_counts())
