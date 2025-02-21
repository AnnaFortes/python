#ESCOPO   
def teste():  #ESCOPO LOCAL
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#PROGRAMA PRINCIPAL - ESCOPO GLOBAL
n = 2
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}') X ESTÁ NO ESCOPO LOCAL

""" SAÍDA: ERRO(POR CAUSA DO ESCOPO, OQ É LOCAL SÓ FUNCIONA NO LOCAL, OQ É GLOBAL FUNCIONA EM TODO O CÓDIGO) 
    print(f'No programa principal, x vale {x}')                ^       
NameError: name 'x' is not defined
"""