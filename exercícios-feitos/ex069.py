#Desafio 69 - Análise de dados do grupo
'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
não continuar. No final, mostre:
> Quantas pessoas tem mais de 18 anos;
> Quantos homens foram cadastrados;
> Quantas mulheres tem menos de 20 anos.
'''
#Variáveis
q = 1
homens = 0
mulheres = 0
maiores = 0

#Início do Programa
while True:
    try:
        idade = int(input(f'Digite a idade da {q}º pessoa: '))
        sexo = str(input(f'Digite o sexo da {q}º pessoa [F|M]: '.lower()))
        if idade > 18:
            maiores += 1
        if sexo in 'm':
            homens += 1
        if sexo in 'f':
            if idade < 20:
                mulheres += 1
        controle = int(input('''Quer continuar? 
    [1] Sim!
    [2] Não!
    '''))
        if controle == 2:
            break
        q += 1
    except ValueError:
        q = 1
        homens = 0
        mulheres = 0
        maiores = 0
        print('Dado inválido, começaremos tudo do zero...')
print(f'{maiores} pessoas tem mais de 18 anos!')
print(f'Há {homens} homens cadastrados!')
print(f'{mulheres} mulheres ainda são menores de 20 anos!')