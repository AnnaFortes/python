from datetime import date

def voto(ano):
    anoAtual = date.today().year
    idade = anoAtual - ano

    if (idade >= 16 and idade < 18) or (idade >= 60):
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade > 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'

print('-'* 30)
anoNasc = int(input('Em que ano você nasceu? '))
print(voto(anoNasc))
print()
 