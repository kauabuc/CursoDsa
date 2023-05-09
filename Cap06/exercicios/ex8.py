dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 4, 'd': 5}


def trocaValores(dicio1, dicio2):
    dicTemp = {}

    for d1key, d2val in zip(dicio1, dicio2.values()):
        dicTemp[d1key] = d2val

    return dicTemp


dict3 = trocaValores(dict1, dict2)
print(dict3)
