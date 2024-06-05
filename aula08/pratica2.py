#Utilização prática do comando from + módulo
from math import sqrt
#Da forma feita acim,a não é necessário utilizar math., somente a função já importada.
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz de {} é igual a {:.2f}.'.format(num, raiz))

