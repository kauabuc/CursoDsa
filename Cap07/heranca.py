class Animal:
    def __init__(self) -> None:
        print("Animal criado")

    def imprimir(self):
        print("Esse é um animal")

    def comer(self):
        print("é hora de comer.")

    def emitir_som(self):
        pass


class Cachorro(Animal):
    def __init__(self) -> None:
        super().__init__()
        print("Objeto cachorro criado")

    def emitir_som(self):
        print("Au au")


class Gato(Animal):
    def __init__(self) -> None:
        super().__init__()
        print("Objeto gato criado")

    def emitir_som(self):
        print("Miau")


cahorro = Cachorro()
gato = Gato()

gato.emitir_som()
cahorro.emitir_som()
