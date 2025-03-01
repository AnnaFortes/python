def metade(p, form= False):
    resul = p / 2
    return moeda(resul) if form else resul

def dobro(p, form=False):
    resul = p * 2
    return moeda(resul) if form else resul

def aumento(p, porc, form=False):
    resul = p - (p * porc / 100)
    return moeda(resul) if form else resul

def reducao(p, porc, form=False):
    resul = p - (p * porc / 100)
    return moeda(resul) if form else resul

def moeda(p):
    return f'R${p:.2f}'.replace('.' , ',')

def resumo(p, taxaAum=10, taxaRed=13):
    print('-' * 50)
    print('RESUMO DO VALOR'. center(50))
    print('-' * 50)
    print(f'Preço analizado: \t\t{moeda(p)}')
    print(f'Dobro do preço: \t\t{dobro(p, True)}')
    print(f'Metade do preço: \t\t{metade(p, True)}')
    print(f'{taxaAum}% de aumento: \t\t{aumento(p, taxaAum, True)}')
    print(f'{taxaRed}% de redução: \t\t{reducao(p, taxaRed, True)}')
    print('-' * 50)

