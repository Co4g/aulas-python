#Prática da aula de Utilização de Módulos
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
# Ao adicionar o math., o próprio programa fornecerá todas as funções importadas em uma lista para ser utilizada.
print('A raíz de {} é igual {:.2f}.'.format(num, raiz))

