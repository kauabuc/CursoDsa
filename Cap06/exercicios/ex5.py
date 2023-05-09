listaA = [2, 3, 4]
listaB = [10, 11, 12]


def elevar(x, y):
    soma = x**y
    print(f"O {x} foi elevado por {y} e resultou em {soma}")
    return y


for i, item in enumerate(listaA):
    elevar(item, listaB[i])
