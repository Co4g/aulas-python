#Desafio 115 - Criando um menu
'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
'''
#Imports
from lib.interface import *
from lib.arquivo import *
from time import sleep

#Corpo do Programa
arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu (['Ver pessoas cadastradas', 'Cadastrar nova pessoa',  'Sair do Sistema'])
    if resposta ==1:
        #Opção de listar o nome de um arquivo
        lerArquivo(arq)
    elif resposta ==2:
        #Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta ==3:
        #opção de sair do sistema
        print(linha())
        print('Saindo do sistema... Até logo!'.center(42))
        print(linha())
        break
    else:
        print('ERRO! Digite uma opção Válida')
    sleep(2)



