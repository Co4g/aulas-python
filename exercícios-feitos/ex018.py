'''
 Faça um programa que leia um ângulo qualquer e mostre na tela
 o valor do seno, cosseno e tangente desse ângulo.
'''
import math
a = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O sen de {}° é: '.format(a), sen)
print('O coseno de {}° é: '.format(a), cos)
print('A tangente de {}° é: '.format(a), tan)
print('O seno, cosseno e tangente de {}° é {:.3}, {:.3} e {:.3} respectivamente.'.format(a, sen, cos, tan))
