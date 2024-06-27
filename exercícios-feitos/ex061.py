#Desafio 61 - Progressão Aritmética v2.0
'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos dessa PA usando a estrutura while.
'''
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 0 #Define contador em 0;
while c < 10: #Define que o loop até o contador atingir 10 (exclusive), para obter só 10 termos da PA.
    print(primeiro_termo) #Inicia mostrando o primeiro termo, do input antes do loop. Será atualizado ao fim do loop.
    primeiro_termo = primeiro_termo + razao #Define a PA como o primeiro termo, mais a razao digitada. 
    c += 1
    #Ao fim do loop, o primeiro_termo será atualizado, garantido o seguimento da PA.

