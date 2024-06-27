#Desafio 97 - Um print especial
'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
e mostre uma mensagem com tamanho adaptável.
'''
#Definição de funções
def escreva(txt):
    print('-'*len(txt))
    print( txt)
    print('-'*len(txt))

texto = input('Digite algo: ')
escreva(texto)