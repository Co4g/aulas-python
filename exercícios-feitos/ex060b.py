'''
Faça um programa que leia um número qualquer e mostre seu fatorial (usando for):
'''

num = int(input('Digite o valor a ser fatorado: '))
fatorado = num #Definimos fatorado como num, para que o primeiro cálculo se o número digitado.
for i in range (num - 1, 0, -1): #Iniciamos a sequência em num -1(7, caso digite 8, por exemplo)
    fatorado =  fatorado * i #Multiplicamos o fatorial, que é o mesmo numero digitado por i, que foi definido acima.
print(fatorado) 
#Sempre que ele fizer o loop, i receberá -1, o que permitira a fatoração.
'''
num = int(input('Digite o valor a ser fatorado: '))
fatorado = 1
for i in range (1, num + 1):
    fatorado *= i
print(fatorado)
'''