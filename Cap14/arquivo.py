import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

dados = pd.read_csv("pytohn/Cursodsa/Cap14/dataset.csv")

# print(dados.shape)
# print(dados.columns)
# print(dados.head())
# print(dados.isnull().sum())
# print(dados["valor_aluguel"].describe())
# print(dados.corr())
# sns.histplot(data=dados, x="valor_aluguel", kde=True)

sns.scatterplot(data=dados, x="area_m2", y='valor_aluguel',)
plt.show()
