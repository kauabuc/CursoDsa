def lista4_elementos(lista):
    if len(lista) < 4:
        print("Por favor envie uma lista de 4 elementos.")
        return

    lista.append(50)
    lista.append(69)
    return print(lista)


lista1 = [0, 1, 2, 3]
lista2 = [1, 2]

lista4_elementos(lista1)
lista4_elementos(lista2)
