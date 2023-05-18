import random

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

dados = sea.load_dataset("tips")
# sea.jointplot(data=dados, x="total_bill", y="tip", kind="reg")
# plt.show()

# sea.lmplot(data=dados, x="total_bill", y="tip", col="smoker")
# plt.show()


df = pd.DataFrame()

df["idade"] = random.sample(range(20, 80), 30)
df["peso"] = random.sample(range(49, 125), 30)

sea.lmplot(df, x="idade", y="peso", fit_reg=True)
plt.show()
sea.kdeplot(df.idade)
