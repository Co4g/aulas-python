#Aula 09 - Manipulando Caracteres
'''
Todas as strings são divididas em pequenos pedaços, que são identificadas pelo Python como números.
Cada número representa um caractere, incluindo espaços, que começam no 0 e vão até onde for necessário.
Um comando que podemos usar é o fatiamente, que identifica, dentro da string da variável, um caractere
Ex: 
'''
#Fatiamento
frase = 'Curso em vídeo Python' #Cada caractere ocupa um pequeno espaço, temos 21 caracteres, do 0 ao 20.
#Para identificar um única caractere, colocamos a variável dentre de colchetes e o número que a representa.
frase [9] #Representa o 10° caractere - pois a contagem começa no 0. Ou seja, a letra 'V' em 'vídeo'.
frase [9:13] #Pega valores entre 9 e 13, não contando o 13, ou seja, as letras 'Víde', ignorando o próprio 13, que é o O.
frase [9:21:2] #O último número, adicionado aqui, faz com que ele pule os números de 2 em 2, ignorando o que está no meio.
frase [:5] #Ele, como não tem um numero antes indicando o começo, começa do 0 e para no 4(o último, não conta).
frase [15:] #Ele mostrará a partir do 15 e como não foi identificado o limite, irá até o último caractere.
frase [9::3] #Como não há nada no segundo número, ele mostrará do 9 até o fim, pulando de 3 em 3.

#Análise

len (frase) #Analisa o comprimento da frase, que mostra a quantidade de caracteres.
frase.count ('o') #Contará quantas vezes a letra 'o' aparece na variável.
frase.count ('o', 0, 13) #O 0 e o 13 delimitam os caracteres em que serão contados as letras 'o'.
frase.find ('deo') #Mostrará em qual caractere começa 'deo', retornando o número do caractere, neste caso, da letra d.
frase.find('Android')#Como a frase Android não esta presente, ele retornará o valor -1.
'Curso' in frase #Retornará verdadeiro ou falso se 'curso' existe na variável frase.

#Transformação

frase.replace('Python', 'Android') #substitui a segunda palavra, pela primeira. Ou seja, Android substituirá Python.
frase.upper() #Torna a frase em maísculo, o que já for maísculo, permanece.
frase.lower() #Troca o que estiver em maísculos, para minisculo.
frase.capitalize() #Torna tudo em minusculo, mas deixa a primeira letra em maíusculo,
frase.title() #Capitaliza palavra por palavra, ao invés só da primeira da frase, como o capitalize.
frase.strip()#Remove caracteres vazios antes e depois da frase. Ou seja, espaços inúteis.
#rstrip, faz o mesmo que o strip, porém remove espaços somente do lado direito, pós frase. lstrip, faz o mesmo do lado esquerdo.

#Divisão
frase.split() 
'''
Divide cada palavra em uma coisa diferente, a partir dos espaços entre elas. Do ponto de vista de contagem de caracteres, 
ao invés de termos 21 caracteres como antes, sempre que trocamos de palavra ele começa a contagem do 0.
'c(0)u(1)r(2)s(3)o(4) e(0)m(1) v(0)í(1)d(2)e(3)o(4)'
Cada uma destas novas divisões, terá um número, também começado em 0. Ou seja, a palavra curso passa a ser o número 0, 
a palavra em o número 1 e assim por diante.
'''

#Junção
'-'.join(frase)
#Faz o inverso da função anterior, retornando a frase a ser uma coisa só, incluindo o total de caracteres que volta a ser 21.
# O uso do '-' representa aquilo que fará a separação de cada palavra dividida na função split. 


 