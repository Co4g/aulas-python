#Desafio 47 - Contagem de Pares
'''
Crei um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
'''
print('Contador de Números Pares')
for c in range(1,51):
    par = c % 2
    if par == 0:
        print(c)
print('Fim do Contador de Pares')
