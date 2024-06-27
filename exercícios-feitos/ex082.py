#Dividindo valores em várias listas
'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie
duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
Ao final, mostre o conteúdo das três listas geradas.
'''
lista = list()
pares = list()
impares = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = int(input('Deseja continuar? [1 -sim / 2 - não]: '))
    if continuar != 1:
        break
for c in range(len(lista)): #Poderia só ter feito for c in lista, o que facilitaria o código abaixo, porém não pensei nisso na hora!
    num = lista [c]
    if num % 2 == 0:
        pares.append(num)
    if num % 2 == 1:
        impares.append(num)
print(f'A lista final ficou da seguinte maneira: {lista}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')