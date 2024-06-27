#Desafio 78 - Maior e Menor valores na lista
'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posições na lista.
'''
lista = []
for c in range(0,5):
    valores = int(input('Digite um número para a lista: '))
    lista.append(valores)
print(f'A lista ficou da seguinte maneira: {lista}')
print(f'O maior número digitado foi {max(lista)} na posição {lista.index(max(lista))}!')
print(f'O menor número digitado foi {min(lista)} na posição {lista.index(min(lista))}!')
    