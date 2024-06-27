#Validando expressões matemáticas
'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu programa
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 
'''
#Este código verifica unicamente a quantidade de parênteses, porém em caso de ordenação errada, ele não funciona!
expre = str(input('Digite uma expressão: '))
expre.split()
aberto = expre.count('(')
fechado = expre.count (')')
if aberto == fechado:
    print('Expressão válida!')
else:
    print('Expressão inválida!')