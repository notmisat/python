from datetime import datetime

warframes = ['Uriel Prime', 'Wisp Prime', 'Sevagoth prime', 'Titania Prime']
for warframe in warframes:
    meu_warframe = f"Nome: {warframe:12} - Número de letras: {len(warframe): 3}" 
    print(meu_warframe)

print()

# Em Python, o simbolo "," não é um separador decimal, para isso, usamos o "."
pi = 3.1415
valor = f'O valor de PI é: {pi:.1f}.'
valor_deslocado = f'O valor de PI deslocado é: {pi:6.1f}.'
valor_preciso = f'O valor de PI mais preciso é: {pi:.4f}.'
print(valor)
print(valor_deslocado)
print(valor_preciso)

print()

data = datetime.now()
minha_data = f'A data de hoje é {data}.'
minha_data_formatada = f'A data de hoje formatda é {data: %d/%m/%Y}.'
print(minha_data)
print(minha_data_formatada)