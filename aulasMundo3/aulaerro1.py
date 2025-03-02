n = int(input('Número: '))
print(f'Você digitou o número {n}')
print()
""" saída: ValueError: invalid literal for int() with base 10: 'oito' 
isso não é um erro e sim uma exceção, ValueError é um erro de valor, ele estava esperando receber um valor inteiro, e acabou recebendo uma string e a palavra oito não pode ser convertido para inteiro pela função int() """