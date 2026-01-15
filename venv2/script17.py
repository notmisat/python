frase = "Em Holvania, existe a melhor farm eficiente de endo e crédito. Viva vania"

# Resultado obtido utilizando o método count diretamente
print("Contagem direta: ", frase.count('vania'))

# Resultado obtido utilizando a quebra da frase em palavras
contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'vania':
        contador += 1
print("Contagem correta: ", contador)