class Estudantes:
    def __init__(self, nome, idade, nota) -> None:
        self.nome = nome
        self.idade = idade
        self.nota = nota


estudantes = Estudantes("Bob", 12, 9.5)
print(estudantes.nome)
print(estudantes.idade)
print(estudantes.nota)


class Funcionarios:
    def __init__(self, nome, salario, cargo) -> None:
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print(
            f"Funcionario(a) {self.nome} tem salário de R$ {self.salario} e o cargo é {self.cargo}")


func1 = Funcionarios("Mary", 20000, "Cientista de Dados")
func1.listFunc()

hasattr(func1, "salario")
setattr(func1, "salario", 4500)
hasattr(func1, 'salario')
getattr(func1, "salario")
func1.listFunc()
