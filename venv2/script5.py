arquivo = open("venv2/dados1.txt", "r")

conteudo = arquivo.readline()

print("Tipo de conteudo:", type(conteudo))

print("Conteudo retornado pelo readline:")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Proximo conteudo retornado:")
print(repr(proximo_conteudo))

arquivo.close()