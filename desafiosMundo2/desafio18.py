frase = str(input('Digite uma frase: ')).strip().lower()
fraseN = frase.split()
fraseJ = ''.join(fraseN)
fraseI =  fraseJ[::-1]

if fraseJ == fraseI:
    print('\nA frase é um palíndromo')
else:
    print('\nA frase não é um palíndromo')
