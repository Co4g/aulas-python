#Análise de dados em tupla
'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
1 - Quantas vezes apareceu o número 9;
2 - Em que posição foi digitado o primeiro valor 3;
3 - Quais foram os números pares.
'''
#Preenchimento da tupla utilizando o método aprendido no exercício 74:
valores = tuple(int(input('Digite um valor: ')) for _ in range(4))
print(f'O número 9 aparece {valores.count(9)} vezes!')
if 3 in valores:
    posicao_tres = valores.index(3)
    print(f'O número 3 aparece pela primeira vez na posição {posicao_tres}')
else:
    print('O número três não foi digitado nenhuma vez!')
#A linha abaixo foi sugestão do chat-GPT, não compreendi totalmente seu uso, mas tentarei praticá-lo!
pares = tuple(valor for valor in valores if valor % 2 == 0)
if len(pares) == 0:
    print('Não há valores pares na tupla!')
else:
    print(f'Os números pares digitados foram: {pares}')