#Aula 20 - Funções (parte 1)
'''
Uma função é um comando que executa algo. No python, já temos diversas funções de fábrica,
como o print(), len(), float(), etc. Porém, também, em caso de precisarmos executar uma rotina,
podemos definir nossas próprias funções, através do def!
'''
 #Por exemplo, para criar uma função que mostrará um mesmo print em diferentes momento do programa, fazemos:
def mostraLinha(): #Damos um nome à função e colocamos um parenteses logo depois.
    print('---'*10) #Este print não será executado neste momento, somente quando for chamado posteriormente.

mostraLinha() #Ao chamarmos a função, ela mostrará aquilo que foi definido acima.
'''
Além disso, podemos também, definir dentro de uma função, nos parenteses, algum comando, para que algo mude.
Por exemplo, definindo título(txt), eu tenho que a função se chama título e tudo aquilo que for colocado
entre pareteses na hora de chamar a função, assumirá o lugar de txt. O txt, por sua vez, deve ser definido 
ainda dentro da função. Isto é chamado de parâmetro:
'''
def título(txt): #Definimos o parâmetro 'txt'
    print('-'*15)
    print(txt) #Aqui é onde text, que será definido na hora que a função for chamada, aparecerá.
    print('-'*15)

título('Olá, mundo!') #Chamamos a função e, no lugar de txt, colocamos a frase. Na hora de executar a função, essa frase substituirá txt.
título('Seja Bem-vindo!')
'''
Da forma que fizemos acima, podemos criar uma variável dentro de uma função, que nos permitirá
executar a mesma função, mudando somente onde for necessário, repetindo os demais processos.
'''