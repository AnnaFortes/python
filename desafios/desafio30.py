#pergunte a distancia de uma viagem em km, calcule o preço da passagem, cobrando 0.50 por km para viagens até 200km e -.45 para viagens mais longas
viagem = int(input('Qual será a distância em km: '))
if viagem <= 200:
    valor = viagem * 0.50
    print(f'O preço da passagem é: {valor :.2f} reais')
else:
    valorL = viagem * 0.45
    print(f'O preço da passagem é: {valorL :.2f} reais')