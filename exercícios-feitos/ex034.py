#Desafio 34
'''
Escreva um programa que pergunte o salário do funcionário e calcule o seu aumento.
Para salários superiores a R$s1.250, calcule um aumento de 10%
Para os inferiores ou iguais o aumento é de 15%.
'''
sal = float(input('Digite seu salário R$'))
if sal > 1250:
    aum = (sal*10) / 100
    print(f'Seu aumento será de R${aum}')
else:
    aum = (sal*15) / 100
    print(f'Seu aumento será de R${aum}')