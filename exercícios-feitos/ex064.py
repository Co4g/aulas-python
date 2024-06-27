#Desafio 64 - Tratando vários valores v1.0
'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles(desconsiderando flag).
'''
while True:
    try:    
        #Solicita o primeiro número para início do loop, estabelece a condição de parada e inicia o contador:
        print('Caso queira encerrar o programa, digite 999')
        num = int(input('Digite um número: '))
        c = 0
        soma = 0
        #Estabelece uma condição if para caso o usuário digite 999 logo de cara:
        if num == 999:
            print('Ok, não iniciaremos o programa!')
            break
        elif num != 999:
            while num != 999:
                c += 1
                soma += num
                num = int(input('Digite outro número: '))
            print(f'Você digitou {c} números e a soma total deles é igual a {soma}!')
            break
    except ValueError:
        print('Dado inválido, digite um número inteiro!')
#A condição if estabelece primeiro n == 999, pois se ele fosse o elif, o print ('ok, não inciaremos o programa') seria executado sempre
print('Programa encerrado!')

