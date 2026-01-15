arquivo_escrita = open("venv2/dados_write.txt", "a")
# necessário colocar o diretório antes do nome do arquivo para seleciona-lo

arquivo_escrita.write("\nConteudo adicional.")
arquivo_escrita.close()