#Função para Fatorial
'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de cálculo de fatorial.
'''
#imports
from time import sleep

#Definições de funções
def fatorial(n, show=False):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    print(f'A fatoração do número {n} resulta em: {resultado}')
    if show == True:
        print(n, end='')
        n -= 1
        while n > 0:
            sleep(0.5)
            print(f' x {n}', end='', flush = True)
            n -= 1
        sleep(0.5)
        print(f' =', resultado)
#Corpo do Programa
while True:
    fat = int(input('Qual número deseja ver o fatorial[999 para parar]? '))
    if fat == 999:
        break
    mostrar = str(input('Deseja mostrar a fatoração? [S/N] '))
    if mostrar in 'Ss':
        mostrar = True
        fatorial(fat, mostrar)
    else:
        fatorial(fat)
fim = 'FIM DA EXECUÇÃO'
print('-='*len(fim))
print(fim.center(len(fim)*2))
print('-='*len(fim))