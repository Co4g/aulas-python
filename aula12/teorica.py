#Aula 12 - Condições Aninhadas
'''
Para criar estruturas aninhadas, você pode simplesmente adicionar novas condições usando
o comando elif, que é um 'senão se', que adiciona uma outra condição além do if e else.
Os elif's podem ser tantos quanto for necessário para conclusão do programa.
Assim como em estruturas condicionais normais, o else é opcional, mesmo com o uso de elif.
'''
nome = str(input('Qual é seu nome? '))
if nome == 'Wesley':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}')
