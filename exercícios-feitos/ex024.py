'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'
'''
cidade = input('Digite o nome de uma cidade: ')
pri_nom = cidade.split()
true_or_false = pri_nom [0].lower() == 'santo'
if true_or_false == True:
    print (f'A cidade {cidade} começa com a palavra santo!')
else:
    print(f'A cidade {cidade} não começa com a palavra santo!')



