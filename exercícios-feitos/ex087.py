#Desafio 87 - Mais sobre Matriz em Python
'''
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
obs: reaproveitarei a sugestão do chat GPT para o exercício anterior, que considerei mais prática, ajustando ela
às novas solicitações do exercício. Porém, reescreverei tudo do zero, ainda que igual.
'''
# Cria uma matriz 3x3 com todos os elementos inicialmente valendo 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

# Itera sobre as linhas da matriz
for i in range(3): #Este range evita os três if que eu utilizei no meu código!
    # Itera sobre as colunas da matriz
    for j in range(3):
        # Substitui o valor atual pela entrada do usuário
        matriz[i][j] = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        #Verifica se o número adicionado é par e incorpora ele à variável soma.
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2] #Soma dos valores da terceira coluna.

#Retorno dos resultados:
print(f'A soma dos números pares da matriz é igual a {soma}!')
print(f'A soma dos números da terceira coluna é igual a {coluna3}!')
print(f'O maior valor da linha dois é {max(matriz[1])}')