import os
        caminho_origem = open("diretorio_trabalho/arquivo_origem.txt", "r")
        arquivo = open(caminho_origem, "r")

# O que aconteceria se o aluno substituísse a utilização do os.path.join por open("diretorio_trabalho/arquivo_origem.txt", "r") para definir o caminho do arquivo?

# R: O código funcionaria apenas em sistema Unix, em que o separador de diretórios é /.