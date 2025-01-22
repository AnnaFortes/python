peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f'Seu IMC é \033[33m{imc :.2f}\033[m, você está \033[33mabaixo do peso!\033[m')
elif imc > 18.6 and imc <= 25:
    print(f'Seu IMC é \033[32m{imc :.2f}\033[m, você está no \033[32mpeso ideal!\033[m')
elif imc >= 26 and imc <= 30:
    print(f'Seu IMC é \033[33m{imc :.2f}\033[m, você está em \033[33msobrepeso!\033[m')
elif imc >= 31 and imc <= 40:
    print(f'Seu IMC é \033[35m{imc :.2f}\033[m, você está \033[35mobeso!\033[m')
else:
    print(f'Seu IMC é \033[31m{imc :.2f}\033[m, você tem \033[31mobesidade morbida!\033[m')