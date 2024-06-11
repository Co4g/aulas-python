#Pratica aula 17
num = [2, 5, 9, 1] #Declaração de uma lista
num [2] = 3 #Substituirá o 9 pelo 3.
num.append(7) #Adiciona o número 7 à lista.
num.sort(reverse=True) #Organiza a lista em ordem, o reverse = True inverte a ordem a lista, começando do 7 até 1.
num.insert(2, 0)#Insere 0 na posição 2.
num.pop() #Exclui o último item da lista.
print(num)
print(f'Essa lista tem {len(num)} elementos.')
#Criando nova lista para outro exemplo:
valores = list() #Ou simplesmente []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
