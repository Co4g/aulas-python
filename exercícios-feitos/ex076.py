#Lista de Preços com Tuplas.
'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
produtos = ('Arroz', 'R$28,00', 'Feijão', 'R$11,99', 'Farinha', 'R$7,59', 'Açucar', 'R$8,60', 'Oleo', 'R$7,89')
produto = 0
preço = 1

print('---'*10)
print('LOJA CO4G'.center(30))
print('---'*10)
for _ in range(5):
    print(produtos[produto].ljust(20, '-'), produtos[preço])
    produto += 2
    preço += 2
