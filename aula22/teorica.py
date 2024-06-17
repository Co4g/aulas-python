#Aula 22 - Módulos e Pacotes
'''
Para tornar os códigos mais legíveis, organizados e menores, podemos adicionar funções externas
criadas por nós mesmos. Para isso, criamos um outro arquivo Python dentro do nosso projeto, que 
armazena nossas funções. Este arquivo python será um módulo, que armazenará nossas funções.
Chamamos as funções, igualmente qualquer outra, usando o import, com o nome do arquivo/módulo.
'''
import modulos

num = int(input('Digite um valor: '))
fat = modulos.fatorial(num)
print(f'O fatorial de {num} é {fat}')
