from functools import reduce


def potencia(x):
    return x**2


numeros = [1, 2, 3, 4, 5]
numerosaoquadros = list(map(potencia, numeros))
print(numerosaoquadros)

temperaturas = [0, 22.5, 40, 100]


def fahrenheit(t):
    return ((float(5)/9)) * (t-32)


def celsius(t):
    return ((float(9)/5) * t+32)


for temp in map(fahrenheit, temperaturas):
    print(temp)

for temp in map(celsius, temperaturas):
    print(temp)


lista = [47, 11, 42, 13]


def soma(a, b):
    x = a + b
    return x


print(reduce(soma, lista))


def verifica_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13, 15, 16, 17, 18, 19]
print(list(filter(verifica_par, lista2)))
print(list(filter(lambda x: x % 2 == 0, lista2)))

x = [1, 3, 5]
y = [2, 4, 6]

print(list(zip(x, y)))
print(list(zip("ABCD", "XYZ")))
