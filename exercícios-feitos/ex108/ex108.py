#Desafio 108 - Formatando moedas em Python
'''
Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga
mostrar os valores como um valor monetário formatado.
'''
import moeda

custo = float(input('Digite um valor: R$ '))
print(f'O dobro de R${custo} é R${moeda.dobro(custo)}') 
print(f'A metade de R${custo} é R${moeda.metade(custo)}')
print(f'O custo de R${custo} com 12% de aumento fica: R${moeda.moeda(moeda.aumentar(custo,12))}')
print(f'O custo de R${custo} com 17% de desconto fica: R${moeda.moeda(moeda.diminuir(custo, 17))}')
