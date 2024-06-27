#Desafio 49 - Tabuada v2.0
'''
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''
num = float(input('Escolha um número para receber sua tabuada:' ))
for c in range(1, 11):
    res = c * num
    print(f'{num} x {c} = {res:.2f}')
