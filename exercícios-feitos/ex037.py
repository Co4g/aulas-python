#Desafio 37 - Conversor de Bases Numéricas
'''
Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão.
1 para binário
2 para octal
3 para hexadecimal
'''
print(30*'\033[31m~~')
print('         CALCULADORA DE BASES NUMÉRICAS')
print(30*'~~')
valor = int(input('\033[32mDigite o valor que deseja converter: '))
conversor = int(input('Digite para qual base deseja converter: \n1 - Binário \n2 - Octal \n3 - Hexadecimal\n'))
if conversor == 1:
    num_conv = bin(valor)[2:]
    print(f'O valor {valor} convertido para binário fica: {num_conv}!')
elif conversor == 2:
    num_conv = oct(valor)[2:]
    print(f'O valor {valor} convertido para octadecimal fica: {num_conv}!')
else:
    num_conv = hex(valor)[2:]
    print(f'O valor {valor} convertido para hexadecimal fica: {num_conv}!')
print(30*'\033[36m~~')
print('           FIM DO PROGRAMA')
print(30*'~~')