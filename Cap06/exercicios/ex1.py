lista = [3, 8, 13]
nova_lista = []


def potenciatres(x):
    x = x**3
    nova_lista.append(x)
    return x


for i in lista:
    potenciatres(i)
print(nova_lista)
