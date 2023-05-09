arq1 = open("pytohn/Cursodsa/Cap06/arquivos/arquivo1.txt", "r")

print(arq1.read())
print(arq1.tell())
print(arq1.seek(0, 0))
print(arq1.read(23))

# arq2 = open("pytohn/Cursodsa/Cap06/arquivos/arquivo2.txt", "w")
# arq2.write("Aprendendo sobre path em python.")
# arq2.close()

# arq2 = open("pytohn/Cursodsa/Cap06/arquivos/arquivo2.txt", "a")
# arq2.write("E a metodologia da Data Science é Incrivel.")
# arq2.close()
# arq2 = open("pytohn/Cursodsa/Cap06/arquivos/arquivo2.txt", "r")
# print(arq2.read())
