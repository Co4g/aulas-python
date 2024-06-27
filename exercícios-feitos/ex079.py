#Valores únicos em uma lista
'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
'''
lista = list()
while True:
    valor = int(input('Digite um valor para a lista: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor repetido, portanto não será adicionado à lista!')
    continuar = int(input('Deseja continuar?[1 - sim/ 2 - não] '))
    if continuar !=1:
        break
print(f'A lista ficou da seguinte maneira: {sorted(lista)}') 
print(f'A lista conta com {len(lista)} elementos!')


    