#Desafio 85 - Listas com pares e ímpares
'''
Crie uma lista onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.
'''
#Declaração de variáveis
num = list()
pares = list()
impares = list()

#Corpo do programa
for c in range(1, 8):
    num.append(int(input(f'Digite o {c}º valor: ')))
num.sort()
for p in num:
    if p % 2 == 0:
        pares.append(p)
    elif p % 2 == 1:
        impares.append(p)
num.clear()
num.append(pares[:])
num.append(impares[:])
print(f'Lista completa: {num}')
print(f'Somente os números pares em ordem crescente: {num[0]}')
print(f'Somente os ímpares na ordem crescente: {num[1]}')
