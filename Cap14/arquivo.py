import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

dados = pd.read_csv("pytohn/Cursodsa/Cap14/dataset.csv")

print(dados.shape)
print(dados.columns)
print(dados.head())
print(dados.isnull().sum())
print(dados["valor_aluguel"].describe())
print(dados.corr())
# sns.histplot(data=dados, x="valor_aluguel", kde=True)

# sns.scatterplot(data=dados, x="area_m2", y='valor_aluguel',)
# plt.show()

y = dados["valor_aluguel"]
x = dados['area_m2']

x = sm.add_constant(x)

modelo = sm.OLS(y, x)

resultado = modelo.fit()

print(resultado.summary())

plt.figure(figsize=(12, 8))
plt.xlabel("area_m2", size=16)
plt.ylabel("valor_aluguel", size=16)
plt.plot(x["area_m2"], y, "o", label="Dados Reais")
plt.plot(x["area_m2"], resultado.fittedvalues, "r-",
         label="Linha de regeressão(Previsão)")
plt.legend(loc='best')
plt.show()
