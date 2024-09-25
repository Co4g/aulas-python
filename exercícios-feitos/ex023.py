'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1

num = input('Digite um número: ')
num = num.rjust(4, '0')
mil = num [0]
cen= num [1]
dez = num [2]
uni = num [3]
print ('O número digitado foi: ', num)
print('Unidade: {} \n Dezena: {} \n Centena {} \n Milhar {}'.format(uni, dez, cen, mil))
'''
while True:
    try:
        num = int(input('Digite um número inteiro entre 0 e 9999: ')) #Solicita o número ao usuário
        if num > 0 and num < 10000: #Verifica se o número está dentro do escopo permitido
            break #Sai do loop, caso o número informado esteja dentro das regras.
        else:
            print('Número fora do escopo permitido, digite um número entre 0 e 9999!') #É chamado, caso o número seja menor ou maior do que o permitido.
    except ValueError:
        print('Dado incorreto, por favor, insira números válidos!') #É chamado caso o dado inserido não seja um número inteiro.

print(f'O número digitado foi {num}, vamos decompô-lo: ')
num = str(num) #Transforma o número em string para manipulação.
num = num.rjust(4, '0') #Preenche os espaços à esquerda do número caso ele não tenha alguma casa com 0.
print(f'Unidade = {num[3]}')
print(f'Dezena = {num[2]}')
print(f'Centena = {num[1]}')
print(f'Milhar = {num[0]}')




