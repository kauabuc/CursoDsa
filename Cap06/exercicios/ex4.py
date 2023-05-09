lista = [0, 1, 2, 3, 4]


def aoquadrado(x):
    x = x**2
    return x


def aocubo(x):
    x = x**3
    return x


for item in lista:
    print(aoquadrado(item))
    print(aocubo(item))
