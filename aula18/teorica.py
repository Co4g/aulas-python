#Aula 18 - Listas Parte 2
'''
Para colocar listas dentro de listas, nós usamos o append, porém usando toda uma lista, ao invés de só adicionar elementos.
Podemos, também, simplesmente declarar a lista dentro da lista, utilizando [[], [], [],...]
'''
#Uma lista simples:
teste = list()
teste.append('Gustavo')
teste.append(40)
#Adicionaremos os elementos da lista teste na lista galera, da seguinte maneira:
galera = list()
galera.append(teste[:])
#A lista galera terá somente um item 0, contendo dois itens nesta posição, uma lista, dentro da outra.

#Já a declaração de listas dentro de listas é feita assim:
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] 
#Na lista acima, temos 4 elementos, com cada um deles contendo outros dois elementos.
print(galera[2][1]) #O [2] referencia a lista maior ['Joaquin', 13], já o [1] referencia o item dentro da lista, o 13.

