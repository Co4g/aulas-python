
#Definição de funções

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(valor, taxa=0, form=True):
    '''
    => Função para determinar o aumento de 10% no valor de um produto
    valor: Parâmetro que será calculado;
    n: Valor do aumento;
    retorno: val_fi, que é o valor já com sua adição. 
    '''
    if form==True:
        n = valor * (taxa/100)
        val_fi = n + valor
        return moeda(val_fi)
    else:
        n = valor * (taxa/100)
        val_fi = n + valor
        return val_fi
    
    
def diminuir(valor, taxa=0, form=True):
    '''
    => Função para determinar a diminuição de 10% no valor de um produto.
    valor: Parâmetro que será calculado;
    n: Valor da diminuição;
    retorno: val_fi, que é o valor já com seu desconto. 
    '''
    if form==True:
        n = valor * (taxa/100)
        val_fi = valor - n
        return moeda(val_fi)
    else:
        n = valor*(taxa/100)
        val_fi = valor - n
        return val_fi

def dobro(valor, form=True):
    '''
    => Calcula o dobro do valor especificado.
    valor: O valor a ser calculado, entrado do usuário.
    retorna: d, o dobro do valor.
    '''
    from moeda import moeda
    if form==True:
        d = valor * 2
        return moeda(d)
    else:
        d = valor*2
        return d
    

def metade(valor, form=True):
    '''
    => Retorna a metade do valor digitado.
    '''
    if form==True:
        m = valor / 2
        return moeda(m)
    else:
        m = valor / 2
        return m

def resumo(valor, juros=0, desconto=0):
    print('-='*20)
    print('Resumo do Valor'.center(40))
    print('-='*20)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do Preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{juros}% de aumento: \t{aumentar(valor, juros)}')
    print(f'{desconto}% de redução: \t\t{diminuir(valor, desconto)}')
    print('-='*20)