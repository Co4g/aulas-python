#Desafio 57 - 
'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F.
Caso esteja errado, peça a digitação novamente, até obter uma resposta válida.
'''

sexo = ''
while sexo.lower() != 'm' and sexo.lower != 'f':
    sexo = input('Digite seu sexo: M/F: ').strip()
    if sexo in ('m', 'M'):
        print('Você é do sexo masculino!')
    else:
        print('Você é do sexo feminino!')
print('Fim')


