'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'
'''
cidade = input('Digite o nome de uma cidade: ')
prinom = cidade.split()
vof = prinom [0].lower() == 'santo'
print (vof)


