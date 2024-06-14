#Parte prática Aula 20

#Defineremos uma função:
def soma(a, b): #A função soma, possui os parâmetros a e b.
    print(f'A = {a} e B {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

#Corpo do programa
#Podemos chamar a função, declarando seus parâmetros de duas formas:
soma(b=4, a=5) #Informamos o parâmetro e seus valores. Se informar b, tem que informar a, se não dá erro!
soma(7,2) #Simplesmente colocando os valores, que assumiram a ordem dos parâmetros definidos no def.

#Também podemos ter um número não definido de parâmetros dentro da uma função definida.
def contador(* num): #Usamos o * para dizer que não sabemos quantos parÂmetros teremos.
    print(num) #Retornará todos os parâmetros especificados na hora de chamar a função.
contador(4, 5, 2, 7, 1) #O parâmetro num assumirá todos estes números, e os colocará dentro de uma lista.