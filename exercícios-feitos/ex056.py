#Desafio 56 - Analisador Completo
'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos.
'''
idade_total = 0 #Armazena a idade total do grupo
soma = 0 #Soma a quantidade de mulheres maiores de 20 anos
mais_velho = 0 #Armazena a idade do homem mais velho
#Loop para obter os dados das 4 pessoas
for c in range(1,5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Digite seu sexo:\n[1] Masculino\n[2] Feminino\n'))
    idade_total =  idade_total + idade #Armazena a idade total do grupo
    mais_velho = idade - mais_velho #Subtrai a idade do mais velho, pela a idade mais recente, para obter um valor de comparação na estrutura if.
    if sexo == 2: #Verifica se é do sexo feminino, para a variável soma
        if idade < 20:
            soma = soma + 1
    elif sexo == 1: #Verifica se é do sexo masculino, para a variável homem
        if mais_velho >= 1: #Se o resultado de mais velho for >=1, então está pessoa é mais velha e seu nome será armazenado na variável homem.
            homem = nome
#Impressão dos resultados:
media = idade_total / 4 #Calcula a media de idade do grupo
print(f'A média de idade do grupo é {media} anos!')
print(f'{soma} mulheres são menores de 20 anos')
print(f'O homem mais velho se chama {homem}!')
