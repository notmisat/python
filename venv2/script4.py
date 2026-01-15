arquivo = open("venv2/dados1.txt", "r")

conteudo = arquivo.read()

print("Tipo de conteudo:", type(conteudo))

print("Conteudo retornado pelo read:")
print(repr(conteudo))

arquivo.close()