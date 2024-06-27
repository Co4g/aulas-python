#Desafio 55 - Maior e menor da sequência
'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
maior = None
menor = None
for c in range (0, 5):
    peso = float(input ('Digite seu peso em kg:  '))
    if maior is None or peso > maior:
        maior = peso
    if menor is None or peso < menor:
        menor = peso
print(maior)
print(menor)