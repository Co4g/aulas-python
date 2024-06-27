#Desafio 94 - Unindo dicionários e listas
'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) A média de idade do grupo.
c) Ums lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da média.
'''
#Declaração de variáveis
p = dict()
ps = list()
mulheres = list()
pam = list()
tot = 0

#Corpo do programa
while True:
    p['nome'] = str(input('Nome: '))
    p['idade'] = int(input('Idade: '))
    p['sexo'] = str(input('Sexo[M/F]: '))
    if p['sexo'] in 'fF':
        mulheres.append(p.copy())
    ps.append(p.copy())
    tot += p['idade']
    continuar = int(input('Deseja cadastrar outra pessoa?[1 - Sim/ 2 - Não]: '))
    if continuar != 1:
        break
média = tot / len(ps)
for i in ps:
    if i['idade'] > média:
        pam.append(i.copy())

#Apresentação de resultados
print(f'O total de pessoas cadastradas foi: {len(ps)}')
print(f'As pessoas cadastradas foram: {ps}')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'As pessoas acima da média de idade foram: {pam}')