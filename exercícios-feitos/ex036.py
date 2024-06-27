#Desafio 36 - Aprovando Empréstimo
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''

print(35*'\033[33m=')
print('Sistema de aprovação de crédito')
print(35*'=')
print('Bem-vindo ao Sistema de Aprovação de Crédito. Iremos fazer algumas perguntas:')
valor_casa = float(input('Digite o valor da casa que deseja adquirir: R$ '))
salario = float(input('Digite o seu salário atual: R$ '))
anos = int(input('Digite em quantos anos deseja pagar: '))
meses = anos * 12
pres_mensal = valor_casa / meses
por_sal = (salario * 30) / 100
if pres_mensal < por_sal:
    print(f'\033[32mParabéns! Seu empréstimo foi aprovado. Sua prestação ficará: R${pres_mensal:.2f} mensais durante {anos} anos!\033[33m')
    print(20*'===')
    print('Obrigado por fazer negócios conosco!')
    print(20*'===\033[m')
else:
    print('\033[31mSeu empréstimo foi negado, pois a parcela mensal ficará acima do teto de 30% do seu salário!\033[33m')
    print(20*'===')
    print('Não perca as esperanças, tente novamente no futuro!') 
    print(20*'===')
    
