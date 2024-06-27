#Desafio 30
'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$-.50 por km para viagens de até 200km
e R$0.45 para viagens mais longas.
'''
print('Olá, nossas viagens seguem as seguintes regras:')
print ('Viagens de até 200km custam R$0.50 por km. \nAcima disto, custam R$0.45 por km')
km = float(input('Digite quantos quilômetros você deseja viajar: '))
if km <=200:
    valor_viagem = km * 0.5
    print(f'Sua viagem de {km}km custará R${valor_viagem:.2f}')
else:
    valor_viagem = km * 0.45
    print(f'Sua viagem de {km}km custará R${valor_viagem:.2f}')