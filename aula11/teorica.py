#Aula 11 - Cores no Terminal
#Podemos adicionar cores usando diversas formas no python, uma delas é usando o código \033[m
#0, 1, 4 e 7 representam o estilo.
#Números do 30 até o 37 representam as cores do texto.
#Números do 40 até 47 representam a cor de fundo.
print('\033[32m')
print('Será que continua assim?')
idade = int(input('Quantos anos você tem?'))