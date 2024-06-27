#Extraindo dados de uma lista
'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) quantos números foram digitados;
b) a lista de valores ordenada de forma decrescente.
c) se o valor 5 foi digita e está ou não na lista.
'''
lista = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = int(input('Deseja continuar? [1 - sim/ 2 - não]: '))
    if continuar != 1:
        break
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O valor 5 foi digitado, está na lista na posição {lista.index(5)}!')
else:
    print('O número 5 não foi digitado, e não está presente na lista!')