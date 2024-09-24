'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Digite quantos quilometros foram rodados: '))
da = int(input('Digite a quantidade de dias alugados: '))
vk = km*0.15 
va = da*60
vt = va+vk
print('O total pelos dias de aluguel foi: R${}!\nO total pela quilometragem rodada foi: R${:.2f}!'.format(va, vk))
print('O valor total a pagar é: R${:.2f}!'.format(vt))
'''
from time import sleep
print('=='*20)
print('SISTEMA DE ALUGUEL DE CARROS'.center(40))
print('=='*20)
print('Olá, seja bem-vindo ao sistema de devolução do seu carro. Pediremos alguns dados:')
print('Tabela de Preços:')
print('Valor por Quilômetros Rodados: R$0.15/km')
print('Valor por dia de aluguel: R$60/d')
while True:
    try:
        nome_cliente = str(input('Por favor, digite seu nome: '))
        placa_carro = str(input(f'{nome_cliente}, informe a Placa do Veículo: '))
        kil_rod = float(input('Quantos quilômetros foram rodados? (Utilize somente número e pontos no lugar de vírgulas!) '))
        dias = int(input('Quantos dias o carro ficou em sua posse? '))
        break
    except ValueError:
        print('Erro de validação. Por favor, digite um dado válido!')
total = dias*60 + kil_rod*0.15
print('Validando dados, aguarde um momento...')
sleep(1)
print('--'*20)
print('Dados do Aluguel'.center(40))
sleep(0.5)
print(f'Cliente = {nome_cliente}')
sleep(0.5)
print(f'Placa do Veículo = {placa_carro}')
sleep(0.5)
print(f'Quilômetros rodados = {kil_rod}km')
sleep(0.5)
print(f'Dias de aluguel = {dias} dias')
sleep(0.5)
print(f'Cáculo da dívida -> Km = R${kil_rod*0.15:.2f} + Dias = R${dias*60}')
print(f'Total a pagar = R${total:.2f}')
print('=_-'*20)
print('Obrigado por fazer negócios conosco. VOLTE SEMPRE!'.center(60))
print('=_-'*20)