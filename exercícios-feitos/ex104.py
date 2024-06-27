#Validando entrada de dados em Python
'''
Crie uma função que chamada leiaint(), que vai funcionar de forma semelhante ao input() do Python,
só que fazendo a validação para aceitar apenar um valor numérico.
ex: n = leaint('Digite um n')
'''
#imports
    #Não foram necessário imports neste programa!
#Definição de Funções
def leiaint(n):
    while True:
        try:
            n = int(input(n))
            break
        except: 
            print('Dado inválido, informe um número!')
    return n

#Declaração de variáveis
num = leiaint('Informe um valor inteiro: ')
#Corpo do Programa
print(f'O valor informado foi: {num}')