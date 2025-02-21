#parametros opcionais
def somar(a=0, b=0, c=0):
    """ 
    -> Faz a soma entre três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(b=4, c=2)
somar(3, 2, 5)
somar(3, 2)
somar()
