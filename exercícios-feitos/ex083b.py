#Novo teste após analisar muito e fazer muitos testes: deu certo!
valor = str(input('Digite uma expressão: '))
aberto = 0
fechado = 0
for c in valor:
    if c == '(':
        aberto += 1
    elif c == ')':
        fechado += 1
        if fechado > aberto:
             break
if aberto != fechado:
        print('Expressão inválida!')
else:
     print('Expressão válida!')
