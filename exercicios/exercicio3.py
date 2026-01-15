def zenit_polar_replace(text):
    # Aplicando codificação ZENIT POLAR utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old,new)
    
    return text

def main():
    # Entrada da frase e aplicação da codificação
    phrase = "A ágil raposa pulou por cima do lento cachorro"
    phrase = phrase.title() # Primeira letra de cada palavra em maiúscula
    words = phrase.split() # Dividir a frase em palavras
    coded_words = [zenit_polar_replace(word) for word in words] # Processar cada palavra na lista usando ZENIT POLAR
    coded_phrase = " ".join(coded_words)
    print("Original: ", phrase)
    print("Codificada: ", coded_phrase)

if __name__ == "__main__":
    main()
