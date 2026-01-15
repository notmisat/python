import os

# para o arquivo dados1.txt
arquivo1 = open("venv2/dados1.txt") # caminho relativo
arquivo2 = (r"C:/EAD/venv2/dados1.txt") # caminho absoluto (r = read)

# para o arquivo dados2.txt
arquivo3 = open("documentos/dados2.txt") #caminho relativo
arquivo4 = open(r"C:/EAD/documentos/dados2.txt") #caminho absoluto (r = read)

print(os.path.relpath(arquivo1.name))
print(os.path.abspath(arquivo1.name))

print(arquivo1)

# Legenda do CTRL ALT N no terminal
# TextIOWrapper, que trata de arquivos de texto.
# Nome do arquivo, name='dados.txt'.
# Modo de acesso ao arquivo, mode='r'.
# Codificação do arquivo, encoding='cp1252'.].