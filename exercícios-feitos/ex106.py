#Interactive helping system in Python
'''
Faça um minisistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: use cores.
'''
#Imports

#Definição de funções
def IHP(função):
    print('-='*20)
    print(f'Manual do comando {função}!'.center(40))
    print('-='*20)
    print(eval(função).__doc__)

#Declaração de variáveis


#Corpo do Programa
while True:
    comando = input('Digite qual função você gostaria de receber o manual: ')
    if comando.upper() == 'FIM':
        break
    else:
        IHP(comando)
    
'''
Não consegui fazer o programa funcionar normalmente, então pedi ao chat uma dica e ele me ensinou o comando eval.
'''
