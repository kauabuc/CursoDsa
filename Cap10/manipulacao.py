import numpy as np
from pandas import DataFrame

dados = {
    "Estado": ['Santa Catarina', "Rio de Janeiro", "Tocantins", "Bahia", "Minas Gerais"],
    "Ano": [2004, 2005, 2006, 2007, 2008],
    "Taxa Desemprego": [1.5, 1.7, 1.6, 2.4, 2.6],
}

df = DataFrame(dados)
# print(df.head())

df2 = DataFrame(dados, columns=["Estado", "Taxa Desemprego", "Taxa Crescimento", "Ano"],
                index=["estado1", "estado2", "estado3", "estado4", "estado5"])

# print(df2['Estado'])


df2['Taxa Crescimento'] = np.arange(5.)
print(df2)
print(df2.describe())
