#Peça uma entrada e fornaça o máximo de informações sobre ela em um print.

a = (input('Digite algo: '));

try:
    float(a)
    is_float = True
except ValueError:
    is_float = False


print('é um número?', a.isnumeric());
print("{} é uma letra?".format (a), a.isalpha())
print(a, 'é um número decimal?',a.isdecimal())
print(a, 'está capitalizado?', a.isupper())
print(a, 'está com letra minuscula?', a.islower())
print(a, 'é um título?', a.isidentifier())
print(a.isalnum())
print('É um número de ponto flutuante?', is_float)
print(type(a))