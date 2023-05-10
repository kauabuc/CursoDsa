import random
from os import name, system


def limpa_tela():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def game():

    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ["banana", "uva", "morango", "abacate", "laranja"]
    palavra = random.choice(palavras)

    letras_descobertas = ["_" for letras in palavra]

    tentativas = 6
    letras_erradas = []

    while tentativas > 0:
        print(" ".join(letras_descobertas))
        print(f"\nTentativas restantes: {tentativas}")
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            if tentativa in letras_erradas:
                print("\nVocê ja tentou essa letra, escreva outra por favor!")
            else:
                letras_erradas.append(tentativa)
            tentativas -= 1

        if "_" not in letras_descobertas:
            print(f"\nVocê venceu a palavra era: {palavra}")
            break

    if "_" in letras_descobertas:
        print(f"\nVocê perdeu a palavra era: {palavra}")


if __name__ == "__main__":
    game()
    print("\nProgramação com a DSA.")
