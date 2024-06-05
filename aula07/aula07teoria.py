#Aula sobre Operadores Ariteméticos
# + Sinal de mais, serve para adição. Já o -, serve para subtração.
# O * asterisco serve para multiplicação, enquanto a barra /, serve para divisões.
# Dois asteríscos representam a potenciação. Enquanto // representa divisão inteira.
# Já a porcentagem %, serve para calcular o resto da divisão.
# Para escrever igual, devemos usar dois sinais de igual ==, pois somente um, significa atribução.
# A ordem de precedência começa, igualmente na matemática, da seguinte forma:
    # Primeiro, os () > ** > *, /, //, % > + e -;

#Exemplos
b=5+3*2
c=3*5+4**2
d=3*(5+4)**2

# Para potência, também pode ser usado uma função chamada pow, seguida de parenteses e os dois números.
a=pow(4,3)
# Para raíz, devemos utilizar a potência, devidido por meio ou menos, da seguinte forma:
e=81**(1/2)
# O resultado acima, deve ser 81 elevado a 0.5, que é o mesmo que obter a raíz quadrada deste número.
f=139**(1/3)
#Acima, obteremos a raíz cubica de 139, e conforme for necessário, diminuindo a divisão, teremos outras raízes.

# Podemos fazer multiplicações com strings, como abaixo:
print("Oi"*10)
# O que ocorrerá neste caso, é que a palavra Oi será multiplicado e aparecerá dez vezes em sequência.

# Para quebra de linhas, utilizamos o \n e para manter tudo na mesma linha, utilizamos o end=''. ex:
print ('Wesley ', end='') 
print('Cardoso de \n Medeiros')
