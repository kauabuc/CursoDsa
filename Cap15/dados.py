import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dados = pd.read_csv("pytohn/Cursodsa/Cap15/dataset.csv")


# variavel de entrada
x = np.array(dados['horas_estudo_mes'])

x = x.reshape(-1, 1)

# Variavel Alvo
y = dados["salario"]

# plt.scatter(x, y, color="blue", label="Dados reais historicos")
# plt.xlabel("Horas de Estudo")
# plt.ylabel("Salário")
# plt.legend()
# plt.show()


x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.2, random_state=42)


modelo = LinearRegression()

modelo.fit(x_treino, y_treino)


plt.scatter(x, y, color="blue", label="Dados reais historicos")
plt.plot(x, modelo.predict(x), color="red",
         label="Reta de regressão com as previsões")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.show()


score = modelo.score(x_teste, y_teste)
print(f"Coeficiente R2 {score:.2f}")

print(modelo.intercept_)  # w0
print(modelo.coef_)  # w1

horas_estudo_novo = np.array([[48]])

salario_previsto = modelo.predict(horas_estudo_novo)

print(
    f"Se você estudar {horas_estudo_novo} horas por mês seu salário poderá ser de {salario_previsto}")

salario = modelo.intercept_ + (modelo.coef_ * horas_estudo_novo)
print(salario)
