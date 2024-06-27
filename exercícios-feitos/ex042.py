#Desafio 42 - Analisando Triângulos v2.0
'''
Refaça o desafio 35 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais;
- Isósceles: dois lados iguais;
- Escaleno: Todos os lados diferentes.
'''
print('Analisando triângulos v2.0!')
print('Para saber se é ou não um triângulo, vamos começar adicionando a medida de seus lados!')
a = float(input('Adicione a medida do primeiro lado, em cm: '))
b = float(input('Adicione a mededia do segundo lado, em cm: '))
c = float(input('Por último, adicione, também em cm, a medida do terceiro lado: '))
if a+b > c and c+a > b and c+b > a:
    print(f'É um triângulo')
    if a == b and b == c and c == a:
        print('Se trata de um triângulo Equilatero!')
    elif a == b or a == c or c == b:
        print('Se trata de um triângulo Isósciles!')
    else:
        print('Se trata de um triângulo Escaleno!')
elif a + b == c and a + c == b and c + b == a:
    print('O segmentos ABC se sobrepoêm, portanto, se trata de um Triângulo Degenerado!')
else:
    print('Não é um triângulo!')