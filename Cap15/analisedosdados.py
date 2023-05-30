import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dados = pd.read_csv("pytohn/Cursodsa/Cap15/dataset.csv")

print(dados.head())
print(dados.columns)

print(dados.isnull().sum())
print(dados.info())
print(dados.corr())

print(dados.describe())

sns.histplot(data=dados, x="horas_estudo_mes", kde=True)
plt.show()
