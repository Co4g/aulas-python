#Contando vogais em Tupla
'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.
'''
tupla = ("Wesley", "Thiago", "Luna", "Sueli", "Alberto", "Aline")
vogais = "aeiouAEIOU"
index = 0
while True:
    if index >= len(tupla):
        break
    palavra = tupla[index]
    v = [letra for letra in palavra if letra in vogais]
    print(f'A palavra {tupla[index]} tem as vogais {v}')
    index += 1
