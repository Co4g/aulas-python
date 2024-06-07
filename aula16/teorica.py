#Aula 16 de Python - Tuplas (Variáveis Compostas)
'''
Variáveis simples ocupam um espaço de memória. Se precisarmos adicionar um novo valor à mesma variável, 
ela eliminará o valor anterior. Já variáveis compostas podem receber quantos valores for necessário.
Existem três tipos de variáveis compostas em Python: Tuplas, Listas e Dicionários. Esta aula visa as Tuplas.
'''
#Ex:
lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim') #Definimos uma tupla colocando os elementos entre parenteses.
#O índice da tupla segue a mesma ordem do fatiamento de strings, começando em zero e seguindo a numeração normal posterior.
print(lanche [2]) 
#Este print mostrará o elemento 2 da tupla, no caso, a pizza.
print(lanche[0:2]) 
#Este print mostrará os elementos do 0 até o 2, ignorando o último. No caso, mostrará Hamburguer e suco.
print(lanche [1:]) 
#Este print mostrará elementos começando pelo 1 e, como não é determinado o final, mostrará os demais elementos posteriores.
print(lanche[-1])
#Ele retornará a lista em 1 vetor, ou seja, voltará ao último elemento da tupla, o pudim.
print(len(lanche))
#Mostrará o comprimento da variável lanche. O retorno será 4.

#Estruturas de repetição
'''
Podemos usar tuplas em estruturas de repetição. No exemplo abaixo, ao utilizarmos o for, podemos evitar o uso 
do range () simplesmente colocando a variável, que é uma tupla. O range então assumirá o len da tupla, no caso (0,5)
Lembrando que o range ignora o último valor, portanto a tupla com len 4, resulta num range (0,5).
''' 
for c in lanche:
    print(c)
#A variável c assume o valor de lanche de acordo com seu índice, começando do 0 (hamburguer), até pudim (4).

#Tuplas são IMUTÁVEIS!