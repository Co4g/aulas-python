#Desafio 65 - Maior e menores valores
'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar os valores.
'''
while True:
    try:
        c = 1
        soma = 0
        num = 0
        maior = 0
        menor = None
        c2 = 0
        while c == 1:
            c2 += 1
            num = int(input('Digite um número: '))
            soma = soma + num
            media = soma / c2
            if num > maior:
                maior = num
            if menor is None or num < menor:
                menor = num
            c = int(input('''Deseja continuar?
                        [1] Sim!
                        [2] Não!
                        '''))
        break
    except ValueError:
        print('Dado inválido, começaremos do zero!')
print(f'A media dos valores que você digitou é {media}, o maior valor é {maior} e o menor é {menor}!')
print('Encerrando programa...')
