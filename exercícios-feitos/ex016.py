'''
Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção inteira.
'''
import math
'''
#Código Original
nr = float(input('Digite um número real: '))
ni = math.floor(nr)
print('A porção inteira do número real informado é {}!'.format(ni))
'''
print('Vamos aprender sobre números inteiros!')
print('Os inteiros, são aqueles que ignoram os números após a vírgula.')

while True:
    try:
        num_usuario = float(input('Digite um número real para exemplo: '))
        num_int = math.floor(num_usuario)
        print(f'Você digitou o número {num_usuario}, mas sua porção inteira é somente aquela antes da vírgula, ou seja, o número {num_int}!')
        resposta = int(input('''Deseja ver outro exemplo? 
                         1 - Sim
                         2 - Não'''))
        if resposta == 2:
            break
    except:
        print('Digite um número válido!')
   
print('Espero que tudo tenha ficado claro. Se tiver dúvidas, volte quando quiser!')