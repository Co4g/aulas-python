#Aula 21 - Funções parte 2 (help)
"""
Para obter os parâmetros de uma função, podemos usar o comando help(função), para exibir uma ajuda
sobre determinada função. Ou também print(função.__doc__), que retornará a documentação daquela função.
"""
print(print.__doc__)
#Para definir o doc de nossas próprias funções, abrimos aspas triplas logo após o def e colocamos nosos manual:
def contador(i, f, p):
    #Logo abaixo, está o manual da função contador, que só será exibido caso seja chamado pelo help().
    """
    > A função faz uma contagem entre o valor inicial(i), final(f) e com um passo(p):
    a) i = o início da contagem(int)
    b) f = o final da contagem (int)
    c) p = o passo da contagem(int, positivo)
    """
    c= i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')
help(contador)
