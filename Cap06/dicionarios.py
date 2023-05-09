import json

dict_guido = {
    "nome": "Guido van Rossum",
    "linguagem": "Python",
    "similar": ["c", "modulo-3", "lisp"],
    "usuarios": 100000
}


with open("pytohn/Cursodsa/Cap06/arquivos/dados.json", "w") as arquivo:
    arquivo.write(json.dumps(dict_guido))

with open("pytohn/Cursodsa/Cap06/arquivos/dados.json", "r") as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)
