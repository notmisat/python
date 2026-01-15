# Qual das opções a seguir é necessária para que o código funcione corretamente
# se os diretórios de destino não existirem inicialmente?

import os
import shutil

def mover_arquivos(diretorio_origem):
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1].lower()
            if extensao in ['pdf', 'txt', 'jpg']:
                diretorio_destino = os.path.join(diretorio_origem, extensao)
                if not os.path.exists(diretorio_destino):
                    os.makedirs(diretorio_destino)
                    shutil.move(caminho_arquivo, diretorio_destino)
                    print(f"{arquivo} movido para {diretorio_destino}.")

# R: Garantir que os.makedirs(diretorio_destino) linha 12, seja chamado antes de shutil.move linha 13