with open("dados13.txt", "r") as arquivo:
    texto = arquivo.read()
    contador = texto.count("Ola")
    print("Total de Olás = ", contador)
