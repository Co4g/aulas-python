'''
Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'a';
Em qual posição ela aparece a primeira vez;
Em qual posição ela aparece a última vez.
'''
frase = input('Digite uma frase aleatória: ')
letra = frase.lower()
print('A letra a aparece {} vezes'.format(letra.count('a')))
print('A letra a aparece pela primeira vez na posição {}'.format(letra.find('a')))
letra = letra [::-1]
print('a letra a aparece pela última vez na posição {}'.format(letra.find('a')))

