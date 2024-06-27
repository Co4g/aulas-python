#Desafio 109 - Formatando moedas em Python
'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.
'''
import moeda

custo = float(input('Digite um valor: R$ '))
formatar = str(input('Deseja formatar o resultado? [S/N]'))
if formatar in 'Ss':
    formato = True
else:
    formato = False
print(f'O dobro de {moeda.moeda(custo)} é {moeda.dobro(custo, formato)}') 
print(f'A metade de {moeda.moeda(custo)} é {moeda.metade(custo, formato)}')
print(f'O custo de {moeda.moeda(custo)} com 12% de aumento fica: {moeda.aumentar(custo,12, formato)}')
print(f'O custo de {moeda.moeda(custo)} com 17% de desconto fica: {moeda.diminuir(custo, 17, formato)}')