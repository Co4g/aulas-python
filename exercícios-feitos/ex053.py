#Desafio 53 - Detector de Palídromo
'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
frase = input('Digite uma frase qualquer: ')
frase_sem_espacos = frase.replace(' ', '').lower()  # Remove espaços e converte para minúsculas
tam = len(frase_sem_espacos)
palindromo = True
for i in range(tam // 2):  # Percorre até a metade da frase sem espaços
    if frase_sem_espacos[i] != frase_sem_espacos[tam - 1 - i]:
        palindromo = False
        break

if palindromo:
    print(f'A frase "{frase}" é um palíndromo!')
else:
    print(f'A frase "{frase}" não é um palíndromo.')
#Admito, esse eu não consegui fazer!