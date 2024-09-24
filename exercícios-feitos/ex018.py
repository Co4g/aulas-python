'''
 Faça um programa que leia um ângulo qualquer e mostre na tela
 o valor do seno, cosseno e tangente desse ângulo.
'''
import math
'''
angulo = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O sen de {}° é: '.format(angulo), sen)
print('O coseno de {}° é: '.format(angulo), cos)
print('A tangente de {}° é: '.format(angulo), tan)
print('O seno, cosseno e tangente de {}° é {:.3}, {:.3} e {:.3} respectivamente.'.format(angulo, sen, cos, tan))
'''

print('=_-'*15)
print('Calculadora de Seno, Cosseno e Tangente'.center(45))
print('=_-'*15)
def angulos(angulo):
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))
    print(f'O seno, cosseno e tangente do ângulo {angulo} são, respectivamente: {seno:.3f}, {cosseno:.3f} e {tangente:.3f}')

ang_usuario = float(input('Digite um ângulo qualquer: '))
angulos(ang_usuario)
