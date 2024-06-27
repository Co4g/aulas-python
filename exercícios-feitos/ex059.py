#Desafio 59 - Criando um menu de opções
'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa
Seu programa deverá executar a operação solicitada em cada caso.
'''
decisao = ''
while decisao in ['','1', '2', '3', '4']:
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    decisao = str(input('''O que deseja fazer com estes dois números?
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] novos números
          [5] Sair do programa
          '''))
    if decisao == '1':
        soma = num1 + num2
        print(f'O resultado da soma entre {num1} e {num2} é {soma}!')
    elif decisao == '2':
        mult = num1 * num2
        print(f'O resultado da multiplicação entre {num1} e {num2} é {mult}!')
    elif decisao == '3':
        if num1 > num2:
            print(f'O maior número é {num1}')
        elif num1 == num2:
            print('Os números são iguais!')
        else:
            print(f'O maior número é o {num2}')
    elif decisao == '4':
        print('Certo, novos números então...')
print('Ok, programa encerrado!')