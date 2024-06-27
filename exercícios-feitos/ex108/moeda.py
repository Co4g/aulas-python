#Módulo para os exercícios da aula 21

'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.
'''

#Definição de funções
#Função aumentar
def aumentar(valor, taxa=10):
    '''
    => Função para determinar o aumento de 10% no valor de um produto
    valor: Parâmetro que será calculado;
    n: Valor do aumento;
    retorno: val_fi, que é o valor já com sua adição. 
    '''
    n = valor * (taxa/100)
    val_fi = n + valor
    return val_fi

def diminuir(valor, taxa=10):
    '''
    => Função para determinar a diminuição de 10% no valor de um produto.
    valor: Parâmetro que será calculado;
    n: Valor da diminuição;
    retorno: val_fi, que é o valor já com seu desconto. 
    '''
    n = valor * (taxa/100)
    val_fi = valor - n
    return val_fi

def dobro(valor):
    '''
    => Calcula o dobro do valor especificado.
    valor: O valor a ser calculado, entrado do usuário.
    retorna: d, o dobro do valor.
    '''
    d = valor * 2
    return d

def metade(valor):
    '''
    => Retorna a metade do valor digitado.
    '''
    m = valor / 2
    return m

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
    


