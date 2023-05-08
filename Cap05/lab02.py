print("\n **************** Calculadora em Python ****************")

while True:
    print("\n Selecione a opção desejada:")
    print("""
    0 - Para sair
    1 - Soma
    2 - Subtração
    3 - Multipliacação
    4 - Divisão   
    """)

    escolha = input("Digite sua opção (1/2/3/4): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    def soma(num1, num2):
        soma = num1 + num2
        return print(f"A soma dos números {num1}, {num2} é igual a {soma}")

    def subtração(num1, num2):
        subtração = num1 - num2
        return print(f"A subtração dos números {num1}, {num2} é igual a {subtração}")

    def multiplicacao(num1, num2):
        multiplicacao = num1 * num2
        return print(f"A multiplicação dos números {num1}, {num2} é igual a {multiplicacao}")

    def divisao(num1, num2):
        divisao = num1 / num2
        return print(f"A divisão dos números {num1}, {num2} é igual a {divisao}")

    match escolha:
        case "0":
            break
        case "1":
            soma(num1, num2)
        case "2":
            subtração(num1, num2)
        case "3":
            multiplicacao(num1, num2)
        case "4":
            divisao(num1, num2)
        case _:
            print("Por favor digite uma operação válida.")
