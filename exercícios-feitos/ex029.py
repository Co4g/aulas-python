#Desaio 29
'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''
velocidade = float(input('Digite a velocidade do seu carro em Km/h: '))
if velocidade >80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! A multa será no valor de R${multa:.2f}')
else:
    print('Parabéns, você está dentro do limite de velocidade!')
