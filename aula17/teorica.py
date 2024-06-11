#Aula teorica de Listas - Curso em Vído de Python
'''
Devido a um cronograma apertado, detalharei menos esta aula em relação a anterior, focando em pontuar as diferenças
entre tuplas e listas.
- A principal diferença se encontra no fato das listas serem mutáveis, diferente das tuplas. Já outra diferença é
na forma de declaração, pois listas são declaradas usando colchetes.
'''
#Declaração de uma lista:
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
#Iremos substituir um dos elementos da lista:
lanche [3] = 'Picolé'
print(lanche) #A saída será a lista declara, porém com picolé no lugar de pudim.
#Para adicionar um item novo na lista, utilizamos o append()
lanche.append('Bolacha') #Adicionará a bolacha na última posição da lista, que passará a ter cinco elementos.
#Para adicionar elementos em uma posição específica na lista, usamos o insert()
lanche.insert(0, 'Cachorro Quente') #Substituirá o hamburguer na posição zero, empurrando ele e os demais para frente.
print(lanche) #Mostrará a lista atuaizada com o cachorro quente e a bolacha em suas novas posições.
#Para exlusão, podemos usar o comando del, ou o método pop, além do remove:
del lanche [3] #Comando del, utilizando o índice.
lanche.pop(4) #Método pop que também utiliza o índice. Se o índice não for específicado, eliminará o último elemento.
lanche.remove('Suco') #Utilizando o elemento ao invés do índice.
#Podemos também criar listas usando o list e o range
valores = list(range(4, 11))

