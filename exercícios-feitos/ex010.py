#Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

'''
#Versão Original
r = float(input('Quanto dinheiro você tem na carteira? '))
di = r//3.27
de = r/3.27
ds = r%3.27
print('Você pode comprar exatamente', de, 'dólares com {} reais'.format(r))
print('Você pode comprar', di, 'dólares inteiros com {}'.format(r), 'e restará', ds, 'em reais')
'''
#Versão refeita
from time import sleep
print('$$'*20)
print('Bem-vindo(a) ao seu conversor de moedas!'.center(40))
print('$$'*20)
while True:
    try:
        reais = float(input('Quantos reais você tem na carteira? R$ '))
        break
    except ValueError:
        print('Erro no valor digitado, por favor, digite apenas números!')
while True:
    print ('Em qual moeda você gostaria de ver o valor que possui?')
    opção = int(input('''
        1 - Dólares
        2 - Euros
        3 - Ienes
        4 - Libras
        5 - Sair do programa
    '''))
    print('--'*20)
    sleep(0.5)
    if opção == 1:
        print('Cotação do dólar: R$5,59')
        print(f'R${reais} = ${reais/5.59:.2f}')
    elif opção == 2:
        print('Cotação do euro: R$5,98')
        print(f'R${reais} = €{reais / 5.98:.2f}')
    elif opção == 3:
        print('Cotação do Iene: R$0,035')
        print(f'R${reais} = ¥{reais/0.035:.2f}')
    elif opção == 4:
        print('Cotação da Libra: R$7,06')
        print(f'R${reais} = £{reais/7.06:.2f}')
    elif opção == 5:
        print('Ok, encerrando programa...')
        sleep(0.5)
        break
print('Fim do Programa, volte sempre!')
