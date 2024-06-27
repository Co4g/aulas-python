#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.
nome = str(input('Digite o nome do aluno: '))
a = float(input('Digite a primeira nota de {}: '.format(nome)))
b = float(input('Digite a segunda nota de {}: '.format(nome)))

m = (a+b)/2
print('A média de {} é:'.format(nome), m)