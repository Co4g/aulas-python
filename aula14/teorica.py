#Aula 14 - Estruturas de repetição, while(enquanto)
'''
Para usar a estrutura enquanto, nós definimos uma condição. Enquanto essa condição
for verdadeira, os comandos abaixo se repetirão.
'''
import time
c = 0
while c < 11:
    print(c)
    c += 1
    time.sleep(1)
print('Fim!')

'''
Outro exemplo, é caso você queira iniciar uma condição que dependa do usuário. Ex:
'''
#Definiremos n e esperaremos o usuário digitar o valor correto para o programa parar.
n = 1
while n !=0: #Definimos que, enquanto n for diferente de 0, o programa continuará rodando.
    n = float(input('Digite um número: ')) #Pedimos um número ao usuário, que passará a ser o valor de n.
print('fim') #Quando o usuário digitar 0, o programa encerrará e pulará para este print.

