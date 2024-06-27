#Desafio 62 - Progressão Aritmética v3.0
'''
Melhore o desafio 61, perguntando ao usuáio se ele quer mostrar mais algum termo.
O programa encerrará quando ele disser que quer mostrar 0 termos. 
'''
#Solicita o primeiro termo e a razão da PA ao usuário:
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termos = int(input('Quantos termos da PA você gostaria de ver? '))
#Inicia o contador em 0
c = 0
#inicia o primeiro loop fixo
while c < termos:
    print(primeiro_termo, end = ' > ')
    primeiro_termo = primeiro_termo + razao
    c += 1
#Definimos novos termos que serão calculados em 1 para iniciar o novo loop e reseta o contador a 1
c = 1
novos_termos = 1
#Este loop sempre será executado, mas, caso o usuário digite zero, ele pulará o calculo de novos termos
while novos_termos > 0:
    novos_termos = int(input('\nQuantos termos extras gostaria de ver? (Digite 0 caso não queira ver mais nenhum): '))
    c = 1
    if novos_termos > 0:
        while c2 < novos_termos + 1:
            print(primeiro_termo, end = ' > ')
            primeiro_termo = primeiro_termo + razao
            c2 += 1
print('Certo, encerrando programa...')