import random
from os import name, path, system


def limpa_tela():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Hangman:
    def __init__(self, palavra) -> None:
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    def esconder_letra(self):
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += "_"
            else:
                rtn += letra

        return rtn

    def adivinha_letra(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)

        else:
            return False

        return True

    def acabou(self):
        return self.ganhou() or (len(self.letras_erradas) == 6)

    def ganhou(self):
        if "_" not in self.esconder_letra():
            return True
        return False

    def status(self):
        print(board[len(self.letras_erradas)])

        print(f"\nPalavra : {self.esconder_letra()}")

        print("\nLetras Erradas : ")
        for letra in self.letras_erradas:
            print(letra,)

        print()

        print("\nLetras Escolhidas : ")
        for letra in self.letras_escolhidas:
            print(letra,)

        print()


def rand_palavra():
    with open(path.join(
            "pytohn/Cursodsa/br-sem-acentos.txt"), "r") as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split("\n")
        palavra = random.choice(palavras)
        return palavra


def main():
    limpa_tela()

    game = Hangman(rand_palavra())

    while not game.acabou():
        game.status()

        user_input = input("\nDigite uma letra: ")

        game.adivinha_letra(user_input)

    game.status()

    if game.ganhou():
        print("\nParabéns você venceu.")

    else:
        print("Game over!! Você perdeu.")
        print(f"A palavra era {game.palavra}")

    print("Foi bom jogar com você!")


if __name__ == "__main__":
    main()
