minha_lista = ('Wisp', 'Torid', 'Marie')

texto1 = ', '.join(minha_lista)
with open('script19a.txt', 'w') as arquivo:
    arquivo.write(texto1)

texto2 = '\n'.join(minha_lista)
with open('script19b.txt', 'w') as arquivo:
    arquivo.write(texto2)
