"""
Exibir Bem vindo a calculadora
Exibir as operações disponiveis
pedir um numero ao usuario e armazenar ele
pedir outro numero ao usuario e armazenar em outra variavel
fazer um match e case dentro da operação escolhida e com seus numeros
exibir o resultado

"""

print("Bem vindo a calculadora a simples")
print("Temos as 4 operações básicas, qual você deseja: + - / *")

operacao = input("Digite a operação desejada: ")
inputnum1 = input("Digite o primeiro numero: ")
inputnum2 = input("Digite o segundo numero: ")

num1 = float(inputnum1)
num2 = float(inputnum2)

match operacao:
    case "+":
        res = num1 + num2
        print(f"O resultado é {res}")
    case "-":
        res = num1 - num2
        print(f"O resultado é {res}")
    case "*":
        res = num1 * num2
        print(f"O resultado é {res}")
    case "/":
        res = num1 / num2
        print(f"O resultado é {res}")
    case _:
        print("Operação inválida")
