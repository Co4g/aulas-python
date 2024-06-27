'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

num = input('Digite um número: ')
num = num.rjust(4, '0')
mil = num [0]
cen= num [1]
dez = num [2]
uni = num [3]
print ('O número digitado foi: ', num)
print('Unidade: {} \n Dezena: {} \n Centena {} \n Milhar {}'.format(uni, dez, cen, mil))




