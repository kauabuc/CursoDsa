'''class Livro():
    def __init__(self):
        self.titulo = "Sapies - Uma breve história da humanidade."
        self.isbn = 998888
        print("Construtor chamado para criar um objeto da classe")

    def imprime(self):
        print(f"Foi criado o livro {self.titulo} com ISBN {self.isbn}")
'''

# livro1 = Livro()

# print(livro1.titulo)
# print(livro1.isbn)
# livro1.imprime()


class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto da classe")

    def imprime(self):
        print(f"Foi criado o livro {self.titulo} com ISBN {self.isbn}")


livro2 = Livro("Poder do habito", 177234)
livro2.imprime()


class Algoritimo():

    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamada ao iniciar classe.")


algo1 = Algoritimo(tipo_algo="Random Forest")
algo2 = Algoritimo(tipo_algo="DeepLerning")

print(algo1.tipo)
print(algo2.tipo)
