#Desafio 86 - Matriz em Python
'''
Crie um programa que crie uma matriz d dimensão 3x3 e preencha com valores lidos
pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
#Declaração de variáveis
matriz = [[0 , 0, 0], [0 , 0, 0], [0 , 0 , 0]]
p1 = 0 #Index da posição na primeira linha
p2 = 0 #Index da posição na segunda linha
p3 = 0 #Index da posição na terceira linha
#Corpo o programa
for c in range(0,9):
    if c < 3:
        matriz [0][p1] = int(input('Digite um valor: '))
        p1 += 1
    if c >= 3 and c < 6:
        matriz [1][p2] = int(input('Digite um valor: '))
        p2 += 1
    elif c >= 6:
        matriz [2][p3] = int(input('Digite um valor: '))
        p3 += 1

#exibindo resultados:
for linha in matriz:
    print(linha)