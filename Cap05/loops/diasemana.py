while True:
    dia = input("Qual é o dia da semana hoje? ")
    if dia == "sabado" or dia == "domingo":
        print("Hoje é dia de descanso!")
    else:
        print("Você precisa trabalhar! Saia do computador.")
        break
