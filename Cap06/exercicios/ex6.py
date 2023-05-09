lista = range(-5, 5)


def negativo(x):
    if x < 0:
        return True
    else:
        return False


print(list(filter(negativo, lista)))
