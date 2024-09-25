'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas;
* O nome com todas minúsculas;
* Quantas letras ao todo (sem considerar espaços);
* Quantas letras tem o primeiro nome.
'''
nome = str(input('Digite  seu nome completo: '))
nma = nome.upper()
print(nma)
nmi = nome.lower()
print(nmi)
nse = nome.replace(" ", "")
print(len(nse))
nd = nome.split()
print(len(nd[0]))

