'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
km = float(input('Digite quantos quilometros foram rodados: '))
da = int(input('Digite a quantidade de dias alugados: '))
vk = km*0.15 
va = da*60
vt = va+vk
print('O total pelos dias de aluguel foi: R${}!\nO total pela quilometragem rodada foi: R${:.2f}!'.format(va, vk))
print('O valor total a pagar é: R${:.2f}!'.format(vt))
