pag = float(input('Preço das compras: '))
print('OPÇÃO DE PAGAMENTO: ')
print('1 - À vista (dinheiro/pix - 10% de desconto)')
print('2 - À vista (cartão) - 5% de desconto')
print('3 - Em 3x ou mais no cartão (20% de juros)')
print('4 - Em até 2x no cartão (sem juros)')
coman = int(input('Digite a opção de pagamento: '))

if coman == 1:
    tot1 = pag - (10 / 100 * pag)
    print(f'O valor a ser pago de R${tot1 :.2f}')
elif coman == 2:
    tot2 = pag - (5 / 100 * pag)
    print(f'O valor a ser pago de R${tot2 :.2f}')
elif coman == 3:
    tot3 = pag + (20 / 100 * pag)
    print(f'O valor a ser pago é de R${tot3 :.2f}')
elif coman == 4:
    print(f'O valor a ser pago não será afetado R${pag :.2f}')
else:
    print('Opção inválida! Por favor, escolha uma opção válida.')
