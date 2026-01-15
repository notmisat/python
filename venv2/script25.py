import os

try:
    os.remove("venv2/teste.txt")
    print("Arquivo removido!")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessor o arquivo")
    print("Descrição", erro)
except IsADirectoryError as erro:
    print("Remove ser apenas para arquivos")
    print("Descrição", erro)

print("Término do programa")