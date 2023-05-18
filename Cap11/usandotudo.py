import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sea

np.random.seed(42)
n = 1000
pct_smokers = 0.2

# Variáveis
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# Dataframe
dados = pd.DataFrame({'altura': altura, 'peso': peso,
                     'flag_fumante': flag_fumante})

# Cria os dados para a variável flag_fumante
dados['flag_fumante'] = dados['flag_fumante'].map(
    {True: 'Fumante', False: 'Não Fumante'})


sea.set(style="ticks")

# lmplot
sea.lmplot(x='altura',
           y='peso',
           data=dados,
           hue='flag_fumante',
           palette=['tab:blue', 'tab:orange'],
           height=7)

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de Fumantes e Não Fumantes')

# Remove as bordas
sea.despine()

# Show
plt.show()
