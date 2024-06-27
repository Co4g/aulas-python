'''
Escreva um programa que converta uma temperatura digita em °C para °F
'''
c = float(input('Digite a temperatura em °C:' ))
f = (c*1.8) + 32
k = c+273.15
print('A temperatura de {}°C é equivalente a {}°F e {}K!'.format(c, f, k))