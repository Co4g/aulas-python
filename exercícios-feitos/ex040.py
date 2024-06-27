#Desafio 40 - Aquele Clássico da Média
'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingia:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
'''
print('Descubra se você está ou não aprovado!')
nome = str(input('Antes, preciso saber seu nome: '))
nota1 = float(input(f'Certo, {nome} digite a primeira nota, por favor: '))
print (f'Nota 1 = {nota1}')
nota2 = float(input('Agora digite a segunda nota, por favor: '))
media = (nota1 + nota2) / 2
print(f'Nota 1 = {nota1}\nNota 2 = {nota2}\nMédia = {media:.2f}')
if media < 5.0:
    print(f'{nome}, infelizmente sua média foi insuficiente. Você está reprovado!')
elif media > 5.0 and media < 7:
    print(f'{nome}, sua média foi insuficiente para aprovação, você terá que fazer a recuperação!')
else:
    print(f'Parabéns, {nome}! Sua média é o suficiente, você está aprovado!')