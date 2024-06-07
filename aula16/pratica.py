#Parte prática da aula de Tuplas do Curso de Python Módulo 3
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#tuplas sendo imutáveis, o comando abaixo, que tenta dar uma nova atribuição ao elemento 1 da tupla não funcionará!
#lanche [1] = 'Refrigerante' (em comentário para evitar erro no resto do programa.)
for c in lanche:
    print(f'Eu vou comer {c}!')
    #O retorno deve ser 4 linhas, com a mesma frase, porém trocando c por cada item da tupla.
print('Comi para caramba!')
#Também podemos usar o for com range da seguinte maneira. O resultado é o mesmo do exemplo acima.
print('-'*50) #Separador para os exemplos.
for cont in range (0, len(lanche)):
#Fazemos o range final receber o len de lanche, no caso, 4!
    print(lanche[cont])
    #O print mostrará a variável lanche, no valor de cont, que iniciará em 0 e terminará em 3, que é o último elemento da tupla.
print('-'*50) #Separador para os exemplos.
#outra forma, para mostrar a posição do elemento dentro da tupla, podemos usar o enumerate:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
    #A variável comida receberá o elemento da tupla e a variável pos receberá o índice deste elemento dentro da tupla.
#Podemos mexer nas tuplas usando alguns comandos:
print(sorted(lanche)) #Mostrará os elementos da tupla em ordem albética. Eles são ordenados pelo comando sorted!
print(lanche.count('Hamburguer')) # Contará quantas vezes o elemento referenciado aparece na tupla.
print(lanche.index('Suco')) #Mostrará o índice(posição) do elemento referenciado.
del(lanche) #Deleta a tupla inteira. Não funciona para deletar um único item.
#Novas tuplas para outros exemplos:
a = (2, 5, 4)
b = (5, 8, 1, 2)
#Se criarmos uma tupla c sendo ela a + b, teremos uma nova tupla que simplesmente será a junção das duas, na mesma ordem.
c = a + b
d = b + a
#a + b cria uma dupla diferente de b + a, portanto c e d não são a mesma coisa!
print(f'Tupla a: {a}')
print(f'Tupla b: {b}')
print(f'Tupla c: {c}')
print(f'Tupla d: {d}')

