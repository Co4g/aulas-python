#Desafio 70 - Estatísticas em produtos
'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final,
mostre:
> Qual é o total gasto na compra;
> Quantos produtos custam mais de R$1000;
> Qual é o nome do produto mais barato.
'''
#Declaração de variáveis
q = 1
soma = 0
caro = 0
barato = None
#Início do programa
while True:
    try:    
        nome = str(input(f'Digite o nome do {q}º produto: '))
        valor = float(input(f'Digite o valor do {q} produto: '))
        q += 1
        soma += valor
        if valor > 1000:
            caro += 1
        if barato == None or barato > valor:
            barato = valor
            produto_barato = nome
        controle = int(input('''Quer continuar?
[1] Sim!
[2] Não!
'''))
        if controle == 2:
            print('Ok, encerrando programa...')
            break
    except ValueError:
        print('Dado inválido, programa encerrado!')
        produto_barato = 'Nenhum'
        break
print(f'O total gasto será: R${soma}')
print(f'A quantidade de produtos que custam mais de R$1000 será de {caro}!')
print(f'O produto mais barato será: {produto_barato}!')
