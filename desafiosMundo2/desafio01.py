from time import sleep
valor = float(input('\nValor do imóvel: '))
salario = float(input('Salário do comprador: '))
qntAno = int(input('Em quantos anos será pago a casa: '))
tempo = qntAno * 12
prest = valor / tempo
apro = salario - (salario * 30 / 100)
print('=-' * 20)
print('AGUARDANDO RESULTADO...')
sleep(2)
print('=-' * 20)
if prest <= apro:
    print('\033[1;32mPARABÉNS!\033[m Seu empréstimo foi \033[1;32mAPROVADO\033[m!')    
else:
    print('Seu empréstimo foi \033[1;31mNEGADO!\033[m')
