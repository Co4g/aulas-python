#aula 06 do curso de Python do site "curso em vídeo" - Tipos Primitivos

#Primeiro tipo primitivo - 'int', referente aos números inteiros

n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
s=n1+n2
#print('A soma vale:',s) - transformado em comentário para evitar interferência no print com format.

#'int' são números inteiros, como: 7, -4, 0, 9875, etc.
#'float' são números de 'ponto flutuante', ou números reais, como: 4.5, 0.076, 15.223, 7.0.
    #A categoria de ponto float inclui os números inteiros, mas o contrário não ocorre.
#'bool' são valores boleanos, ou lógicos, ou, resumindo, verdadeiro ou falso, representados por: True e False
    #detalhe que True e False devem ser escritos desta exata forma, com letra maiscula no início e depois minusculas.
#'str' são as strings, correspondentes a valores de caracteres, como: 'Olá', '7.5', ''
    #detalhe que mesmo números inteiros ou flutuantes, se estiverem entre aspas, se tornam strings.

#outra sintaxe para o comando print mostrado acima:

print('A soma vale {}'.format(s))
