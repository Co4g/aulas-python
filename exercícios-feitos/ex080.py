#Lista ordenada sem repetições
'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort). No final, mostre a lista ordenada na tela.
'''
import bisect
lista = list()
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    bisect.insort(lista, valor)
    print(f'O valor {valor} foi inserido na posição {lista.index(valor)}')
print(lista)