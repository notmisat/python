# Questão: Desenvolver uma solução para o problema da contagem da palavra “amo” na frase “Eu amo comer amoras no café da manhã.”

frase = "Eu amo comer amoras no café da manhã."
lista_termos = frase.split()

# Solução

contagem = lista_termos.count("amo")
print("Contagem = ", contagem)
