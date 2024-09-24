'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#Código original
import math
co = float(input('Digite o valor do Cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = math.sqrt(math.pow(co, 2)+math.pow(ca, 2))
print('A hipotenusa possui o valor de {:.2f}cm!'.format(hp))
'''
#Código novo
def hipotenusa(cat_op, cat_adj): #Parâmetros recebem o valor dos catetos
        hipotenusa = cat_op*cat_op + cat_adj*cat_adj #Cácula o valor da hipotenusa
        return hipotenusa
while True:
        try:
            co = float(input('Digite o valor do Cateto Oposto: '))
            ca = float(input('Digite o Valor do cateto adjascente: '))
            break
        except ValueError:
            print('\033[31mDado inválido, digite somente números!\033[m')
print(f'O valor da hipotenusa do Cateto Adjascente {ca} e do Cateto Oposto {co} é {hipotenusa(co, ca):.2f}')