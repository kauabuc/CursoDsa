try:
    8 + "s"
except TypeError:
    print("Operação não permitida")

try:
    f = open("pytohn/Cursodsa/Cap06/arquivos/testandoerros.txt", "w")
    f.write("Gravando no arquivo")
except IOError:
    print("Erro: Arquivo não encontrado ou nao pode ser salvo.")
else:
    print("Arquivo salvo com sucesso")
    f.close()
finally:
    print("Vai ser sempre executado")


def askint():
    while True:
        try:
            val = int(input("Digite um numero: "))
        except:
            print("Você não digitou um número.")
            continue
        else:
            print("Obrigado por digitar um numero")
            break
        finally:
            print("Obrigado!")
        print(val)


askint()
