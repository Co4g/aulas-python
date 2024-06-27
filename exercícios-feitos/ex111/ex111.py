#Desafio 111 - Transformando módulos em pacotes
'''
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos
chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107,
108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''
import moeda
import dado
while True:
    try:
        valor = dado.leiadinheiro('Digite o valor: R$')
        aum = int(input('Digite a porcentagem de aumento: '))
        dim = int(input('Digite a porcentagem do desconto: '))
        break
    except ValueError:
        print('Dados inválidos, começaremos do início!')

print(moeda.resumo(valor, aum, dim))

"""
Resolução do exercício 12, já que o 11 somente pedia a criação de pastas.
"""