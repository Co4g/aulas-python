#Desafio 48 - Soma ímpares múltiplos de três
'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''
soma = 0
for c in range(1, 500):
    impar = c % 2
    if impar == 1:
        mult = c % 3
        if mult == 0:
            soma = soma + c
print(soma)