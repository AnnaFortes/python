#faça um programa que leia um número e mostre na tela seu sucessor e seu antecessor.
numero = int(input('Digite um número: '))
antes = numero - 1
depois = numero + 1
print(f'Antecessor: \033[1;35;46m{antes}\033[m\nSucessor: \033[1;36;47m{depois}\033[m')