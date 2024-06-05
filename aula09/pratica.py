#Exemplos práticos da aula 09 de manipulação de frases.
frase = 'Curso em Video Python'
nome = '  Meu nome é Wesley Cardoso de Medeiros  '
print(frase[3]) #Deve retornar a letra s, lembrando que a contagem começa no 0.
print(frase[3:13]) #Deve mostrar da letra s, que é o 3, até o 'e' de vídeo, que é o 12.
print(frase[:15]) #Deve mostrar do zero, já que não é específicado o início, até o 14, que é o o de vídeo.
print(frase[1::2]) #Mostrará do 1 até o fi, pulando de 2 em 2. 
print(nome.count('W')) #Deve retornar quantos W possuí a variável nome. Há diferenciação entre maiusculas e minusculas.
print(len(nome)) #Deve retornar a quantidade de caracteres em nome.
print(len(nome.strip())) #O mesmo que o de cima, porém ignora os espaços inúteis antes e depois.
nome = nome.replace('Wesley', 'Bryan')
print(nome)
#Acima fizemos uma troca e atribuimos permanentemente a mudança em nome.
#Se fizermos o replace dentro do print, a mudança não fica salva e quando usar de novo o nome, ele manterá Wesley.

idade = 'Eu tenho 25 anos de idade'
print(idade.split()) # Devidirá a frase em listas.
outra = 'Eu moro em pelotas'
endereço = outra.split()
print(endereço) #Mostrará a variável endereço dividida também, mas nos permite manipulá-la.
print(endereço [1]) # Mostrará a palavra 0 da lista.
print(endereço[3][3]) #Mostrará o item 3 da lista e a terceira letra deste item.