import os

texto = "Cientista de dados pode ser uma bela profissão. \n"
texto = texto + "Esses profissionais sabem como programar em python. \n"
texto += "E, Claro, devem ser profissionais em Data Science"

arquivo = open(os.path.join(
    "pytohn/Cursodsa/Cap06/arquivos/cientista.txt"), "w")

for palavra in texto.split():
    arquivo.write(palavra + " ")

arquivo.close()

arquivo = open(os.path.join(
    "pytohn/Cursodsa/Cap06/arquivos/cientista.txt"), "r")
conteudo = arquivo.read()
arquivo.close()

with open(os.path.join(
        "pytohn/Cursodsa/Cap06/arquivos/cientista.txt"), "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)
