#Aula 19 - Dicionários
'''
São estruturas de dados semelhantes às tuplas e listas, porém seus índices podem receber nomes.
Os dicionários são identificados por {}. Os espaços do dicionário são chamados de keys.
'''
#Podemos declarar um dicionário da seguinte forma:
dados = dict()
#Ou, atraves das chaves:
dados2 = {'nome':'Pedro', 'idade': 25}
print(dados2['nome']) #Retornará Pedro, que é o nome alocado ao índice 'nome'.
print(dados2['idade'])#Retornará 25
#Para adicionar elementos, podemos simplesmente definir este elemento já com seu valor:
dados2['sexo'] = 'm'
#Para eliminar, podemos usar o del:
del dados2['idade']
#É importante entender a diferença entre valores, chaves e itens:
filme = {'titulo': 'Star Wars', 'Ano':1997, 'diretor':'George Lucas'}
'''
No exemplo acima, temos as seguintes definições:
a) Os valores, sãos aqueles que estão dentro das keys: 'Star Wars', 1997, 'George Lucas'
b) As keys. são o espaço onde os valores estão guardados: 'titulo', 'ano', 'diretor'.
c) Itens, são as keys com seus respectivos valores, exatamente como foi declarada no dicionário.
Portanto, o item {'titulo':'Star Wars'}, possui o valor {'Star Wars'} armazenado na chave '{titulo'}!
'''
print(filme.values()) #Retornará o 'Star Wars', 1997 e 'George Lucas'
print(filme.keys()) #Retornará 'titulo', 'ano' e 'diretor'.
print(filme.items()) #Retornará todo dicionário.
#Usando keys e values em laços:
for k, v in filme.items(): #O laço percorrerá os itens, indo pela keys(k) e depois valores(v).
    print(f'O {k} é {v}')
#Podemos, ainda adicionar dicionários a listas:
locadora = list() #Criamos a lista locadora.
locadora.append(filme) #Adicionamos o dicionario filme à lista locadora.
filme2 = {'titulo':'Avengers', 'ano':2012, 'diretor':'Joss Whedon'}
locadora.append(filme2)
filme3 = {'titulo': 'Matrix', 'ano':1999, 'diretor':'Wachowski'}
locadora.append(filme3)
'''
Os dicionários são referenciados de acordo com o nome que foi dado a sua key ou ao seus value.
Porém, mesmo adicionados às listas, eles mantém esse referencial, enquanto as listas mantém seus 
valores sendo numéricos. Como adicionamos três filmes, cada um assumirá seu lugar na lista, [0, 1, 2].
'''
#Para fazer prints, referenciamos o lugar na lista e a key do valor:
print(locadora[0]['ano']) #retornará o ano do filme alocado no índex 0: 1977
print(locadora[2]['titulo']) #retornará o título do item alocado no índex 2: 'Matrix'

