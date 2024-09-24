"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
a = float(input('Digita o valor do produto em reais: '))
d = (a*5)/100
print(f'O desconto total do produto é igual a: R${d:.2f} reais')