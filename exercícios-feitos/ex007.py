#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.
'''
#Código original
nome = str(input('Digite o nome do aluno: '))
a = float(input('Digite a primeira nota de {}: '.format(nome)))
b = float(input('Digite a segunda nota de {}: '.format(nome)))

m = (a+b)/2
print('A média de {} é:'.format(nome), m)
'''
#Versão revisada
print('-+'*20)
print('SISTEMA DE NOTAS'.center(40))
print('-+'*20)
while True:
    try:
        nome = str(input('Qual é o nome do aluno? '))
        n1 = float(input('Qual a pimeira nota do aluno? '))
        n2 = float(input('Qual a segunda nota do aluno? '))
        break
    except ValueError:
        print('Por favor, digite um dado válido!')
media = (n1+n2)/2
if media >= 6:    
    print(f'A média do aluno {nome} é igual a {media:.2f} e ele está aprovado!')
else:
    print(f'A média do aluno {nome} é igual a {media:.2f} e ele está reprovado!')