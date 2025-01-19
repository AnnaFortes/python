carro = float(input('\nQual é a velocidade do carro? '))
if carro <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    total = 7 * (carro - 80)
    print(f'MULTADO! Você exedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${total :.2f}! \nTenha um bom dia! Dirija com segurança!' )
    