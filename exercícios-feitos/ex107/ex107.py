#Desafio 107 - Exercitando módulos em Python
'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.
'''
import moeda

custo = float(input('Digite um valor: R$ '))
print(f'O dobro de R${custo} é R${moeda.dobro(custo)}') 
print(f'A metade de R${custo} é R${moeda.metade(custo)}')
print(f'O custo de R${custo} com 12% de aumento fica: R${moeda.aumentar(custo,12):.2f}')
print(f'O custo de R${custo} com 17% de desconto fica: R${moeda.diminuir(custo, 17):.2f}')

