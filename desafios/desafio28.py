#ler a velocidade de um carro, se ultrapassar 80km, mostre mensagem dizendo que ele foi multado, a multa vai custar 7reais por cada km acima do limite
carro = int(input('\nQual é a velocidade do carro? '))
if carro <= 80:
    print('Sem multas')
else:
    total = 7 * (carro - 80)
    print(f'Você foi multado e a multa é de {total}')
    