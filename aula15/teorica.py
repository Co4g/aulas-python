#Aula 15 de Python - Laços de Repetição Parte 3 (interrompendo repetições While)
'''
O comando While, se repete ininterruptamente enquanto for verdadeiro. 
Para interrompê-lo, podemos utilizar o comando 'break'.
'''
#No exemplo abaixo, o while se torna falso, assim que cont chega a 10, interrompendo o loop.
cont = 1
while cont <= 10:
    print(cont, '... ', end= '')
    cont += 1
print('Acabou!')
#Já no exemplo abaixo, while nunca será falso, pois não há uma condição para isso, portanto o programa rodará pra sempre.
while True:
    print(cont, '>', end='')
print('Acabou')
#Agora, adicionando uma condição de parada, conseguimos evitar o loop.
n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: #Adicionamos uma condição de que, se o número digitado for 999, o programa se encerrara.
        break #O comando break trata de encerrar o loop, pulando para fora do while.
    s += n
print(f'A soma vale {soma}!')