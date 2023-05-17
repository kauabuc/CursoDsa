import matplotlib.pyplot as plt

x = [7, 2, 2, 13]
atividades = ["dormir", "comer", "passear", "trabalhar"]
cores = ["olive", "lime", "violet", "royalblue"]


# plt.scatter(x, y, label="Pontos", color="black")
# plt.legend()
# plt.show()


plt.pie(x, labels=atividades, colors=cores, startangle=90,
        shadow=True, explode=(0, 0.2, 0, 0))
plt.show()
