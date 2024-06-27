#Desafio 98 - Função de contador.
'''
Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Uma contagem personalizada pelo usuário.
'''
from time import sleep
#Definição de funções
def contador(i, f, p):
    if f > i:
        for c in range(i, f, p):
            sleep(0.5)
            print(c, end=' ', flush=True)

        print()
    else:
        for c in range( i, f, -p):
            sleep(0.5)
            print(c, end=' ', flush=True)
#Corpo do Programa
inicio = 1
fim = 11
passo = 1
contador(inicio, fim, passo) #Por idiotice minha, criei variáveis ao invés de só colocar os números nos parâmetros!
inicio = 10
fim = -2
passo = 2
contador(inicio, fim, passo) #Não satisfeito em fazer bobagem uma vez, fui lá e fiz de novo, mas vai ficar assim!
print()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if inicio > fim:
    contador(inicio, fim-1, passo)
else:
    contador(inicio, fim+1, passo)

'''
Para solução deste problema, utilizei a função contador() com três parâmetros: i, f e p. Criei então um
if para caso o início fosse maior que o fim, onde ele simplesmente mostra o número, dentro do range, normalmente.
Para o caso de o início ser menor que o fim, ou seja, uma contagem regressiva, defini um a condição em que
o passo se tornaria negativo, fazendo o caminho inverso sem problemas.    
Por fim, na hora de executar os resultados, tive um problema com o imput do usuário, pois o range
ignora o último número e eu precisava que ele fosse considerado. Então defini que, caso a conatgem
seja sucessiva, fim receberá +1, para que a contagem encerre no número digitado para fim. E, caso
seja uma contagem regressiva, defini fim recebendo -1, para a contagem encerre no número definido.
Ex: Se o paraâmetro final de uma sucessiva, início 0, for 10, com passo 2, o fim receberá 11, para que a contagem 
escreva também o 10, caso o contrário, pararia no 8. Se o final de uma regressiva, início 10 for 2, com o mesmo
passo, ele pararia no 4, então faço fim -1, para que ele considere o fim como 1, assim o 2 também será considerado.
Cometi um erro bobo de criar variáveis desnecessárias para os parâmetros que já foram pré-definidos no enunciado,
quando eu poderia só ter adicionado os números diretamente dentro do contador()
'''