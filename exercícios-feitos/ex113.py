#Desafio 113 - Funções aprofundadas em Python
'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            break
        except (ValueError, TypeError):
            print('Há um erro no dado inserido, por favor, digite um valor inteiro válido! ')
    return n

def leiaFloat():
    while True:
        try:
            n = float(input('Digite qualquer número: '))
            break
        except ValueError:
            print('O tipo de dado que você inseriu é inválido. Por favor, insira somente números!')
    return n

numero = leiaFloat()
inteiro = leiaInt()
print(numero, inteiro)
