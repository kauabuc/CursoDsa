import csv

with open("pytohn/Cursodsa/Cap06/arquivos/numeros.csv", "w") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(("nota1", "nota2", "nota3"))
    writer.writerow((63, 87, 95))
    writer.writerow((61, 79, 76))
    writer.writerow((72, 64, 61))

with open("pytohn/Cursodsa/Cap06/arquivos/numeros.csv", "r",
          encoding="utf8", newline="\r\n") as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)


with open("pytohn/Cursodsa/Cap06/arquivos/numeros.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

for linha in dados[1:]:
    print(linha)
