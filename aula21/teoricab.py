#Aula 21 - Funções parte 2 (parâmetros opcionais)
'''
Caso criemos uma função com parâmetros que não são prrenchidos na hora da chamada,
nosso programa daria erro neste momento. Para evitar este erro, criamos parâmetros opcionais,
prrenchendo estes vazios na hora de chamar o programa e garantindo que a função funcione, 
mesmo que sejam aplicados parâmetros errôneos.
def soma(a, b, c):
    s = a + b + c
    print(s)
Na função acima, definimos que soma, somará os valores de a, b e c, mas e se na hora de fazer a chamada,
o c não for digitado? ou o também o b? Isso resultaria em um erro, para isso, definimos valores aos parâmetros,
permitindo que, mesmo que nada seja digitado, a variável s tenha valores para utilizar na soma. Vamos a função real:
'''
def soma(a=0, b=0, c=0): #definimos 0 como o valor padrão para os parâmetros.
    s = a + b + c #Se na hora de executar a função, algum parâmetro não for fornecido, ele valerá zero.
    print(s) #A conta será feita normalmente, pois os valores faltantes, serão substituidos por 0.

soma(8, 2) # somente a=8 e b=2 foram fornecidos, mas como c vale zero, a soma será 10, sem problemas.
soma() #Como nenhum parâmetro for fornecido, e todos valem 0 por padrão, a soma será 0.
