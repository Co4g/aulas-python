'''
Este código permite ler o código fonte de algum módulo!
'''

import  inspect
import random
modulo = inspect.getmodule(random)
código_fonte = inspect.getsource(modulo)

print(código_fonte)