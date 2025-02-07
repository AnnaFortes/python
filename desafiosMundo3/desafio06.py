palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

vogais = 'a', 'e', 'i', 'o', 'u'

for palavra in palavras:
    temVogal = ''
    
    for letra in palavra:
        if letra in vogais and letra not in temVogal:
            temVogal += letra
            
    print(f'Na palavra {palavra.upper()} temos {' '.join(temVogal)}')


  
    
