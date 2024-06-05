'''
Aula 10 do curso de Python, sobre estruturas condicionais If\Else
'''
#If e else são condicionais, que querem dizer se\então
#Ao utilizar eles, podemos criar dois caminhos para o programa seguir, dependendo de alguma condição apresentada.
nome = str(input('Qual o seu nome? '))
nome2 = nome.lower().strip()
if nome2 == 'wesley':
    print(f'Que nome lindo você tem, {nome.strip()}!')
else:
    print(f'Que nome feio você tem, {nome.strip()}!')

