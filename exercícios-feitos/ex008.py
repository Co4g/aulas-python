#Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.
'''
#Programa Original
m = float(input('Digite sua altura em metros: '))
cm = m*100
mm = m*1000

print('Sua altura em centímetros é:', cm,'cm')
print('Sua altura em milímetros é:', mm,'mm')
'''
#Versão atualizada
from time import sleep
print('##'*20)
print('CONVERSÃO DE ESCALA'.center(40))
print('##'*20)
while True:
    try:
        m = float(input('Digite um valor em metros: '))
        break
    except ValueError:
        print('ERRO de valor, digite somente números.')
print('Fazendo conversão, aguarde...')
sleep(0.8)
print(f'{m}m é igual a {m*100:.0f}cm e {m*1000:.0f}mm')
sleep(0.5)
print('Obrigado, volte sempre!')