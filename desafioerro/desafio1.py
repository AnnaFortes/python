def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados!\033[m')
            return 0

        else:
            return valor
        

def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
    
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido!\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados!\033[m')
            return 0

        else:
            return valor
                  

print('-' * 35)
n = leiaInt('Digite um Inteiro: ')
nF = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {n} e o real foi {nF}')

print('\033[32mVolte sempre :)\033[m')
print('-' * 35)
print()
    