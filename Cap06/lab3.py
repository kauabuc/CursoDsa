import re

musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''

resultadoA = len(re.findall("a", musica))
print(resultadoA)

resultadoB = len(re.findall("tempo", musica))
print(resultadoB)

resultadoC = re.findall(r'\w+!', musica)
print(list(resultadoC))

resultadoD = re.findall(r'esse\s(\w+)\samargo', musica)
print(resultadoD)

resultadoE = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)
print(resultadoE)
