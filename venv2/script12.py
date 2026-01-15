import os

print("Iterando sobre o arquivo")

with open(r"C:\EAD\venv2\dados1.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo", os.path.basename(arquivo.name))
    # os.path.basename = exibir somente o nome do arquivo (linha 8), sem o caminho (linha 5).