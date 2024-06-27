'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
ex: Ana Maria de Souza
primeiro = ana
último = Souza
'''
nome_completo = input('Digite seu nome completo: ')
nome = nome_completo.split()
pnome = nome [0]
unome = nome [-1]
print('Seu primeiro nome é: {}'.format(pnome))
print('Seu último nome é: {}'.format(unome))
