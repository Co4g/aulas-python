#Desafio 72 - Número por Extenso
'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-la por extenso.
'''
#Declaração da tupla com todos os números entre 0 e 20.
extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", 
           "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", 
           "dezenove", "vinte")
#O index assumirá o valor que o usuário quer mostrar por extenso.
while True:
    index = int(input('Digite um número entre 0 e 20: '))
    if 0 <= index <=20:
        break
    #O print mostrará a variável extenso, no index indicado pelo usuário na linha anterior. Como os números começam em zero, o valor será correspondente.
print(f'Você digitou o número {extenso [index]}!')
