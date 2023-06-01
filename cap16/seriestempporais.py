import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

dados = pd.read_csv("pytohn/Cursodsa/cap16/dataset.csv")
print(dados.shape)
print(dados.columns)
print(dados.info())

dados["Data"] = pd.to_datetime(dados["Data"])

print(dados.head())
print(dados.info())

serie_temporal = dados.set_index("Data")["Total_Vendas"]
serie_temporal = serie_temporal.asfreq("D")
print(serie_temporal)

plt.figure(figsize=(12, 6))
plt.plot(serie_temporal, color="white", linewidth=2)

plt.gca().set_facecolor("#2e03a2")
plt.grid(color="yellow", linestyle="--", linewidth=0.5)

plt.xlabel("Data", color="black", fontsize=14)
plt.ylabel("Vendas", color="black", fontsize=14)
plt.title("Serie Temporal de Vendas", color="black", fontsize=18)

plt.tick_params(axis="x", colors="black")
plt.tick_params(axis="y", colors="black")

plt.show()


modelo = SimpleExpSmoothing(serie_temporal)

modelo_ajustado = modelo.fit(smoothing_level=0.2)

suavizacao_exponencial = modelo_ajustado.fittedvalues


plt.figure(figsize=(12, 6))
plt.plot(serie_temporal, label="Valores reais")
plt.plot(suavizacao_exponencial, label="Valores Previstos", linestyle="--")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.title("Modelo de suavização")
plt.legend()
plt.show()

num_previsoes = 1
previsoes = modelo_ajustado.forecast(steps=num_previsoes)

print("Previsão para janeiro de 2024: ", round(previsoes[0], 4))
