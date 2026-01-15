arquivo = open("venv2/dados1.txt", "r")

conteudo = arquivo.readline()

print("Tipo de conteudo:", type(conteudo))

print("Conteudo retornado pelo readlines:")
print(repr(conteudo))

arquivo.close()