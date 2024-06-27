#Desafio 89 - Boletim com listas compostas
'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
'''
from time import sleep
#Declaração de variáveis
alunos = list()
total = list()
#Corpo do Programa
while True:
    alunos.append(str(input('Nome do aluno: ')))
    alunos.append(float(input('Nota 1 do aluno: ')))
    alunos.append(float(input('Nota 2 do aluno: ')))
    continuar = int(input('Deseja cadastrar outro aluno? [1 - Sim/ 2 - Não]'))
    total.append(alunos[:])
    alunos.clear()
    if continuar != 1:
        break
print('-'*10)
print('Agora, vamos às médias: ')
sleep(0.5)
#Mostra dos resultados:
for i in total:
    media = (i[1] + i[2]) / 2
    print(f'A média do aluno {i[0]} foi {media}!')
    sleep(0.5)
    ver_notas = int(input(f'Deseja ver as notas de {i[0]}? [1 - Sim/ 2 - Não]'))
    sleep(0.5)
    if ver_notas == 1:
        print(f'As notas de {i[0]} foram: {i[1]} e {i[2]}')
        sleep(0.5)
    print('¬¬¬'*5)
sleep(0.5)
print('Pograma encerrado, obrigado por usar!')
