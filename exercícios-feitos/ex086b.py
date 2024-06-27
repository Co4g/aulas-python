#Solução para o exercício sugerida pelo Chat-GPT
'''
Imaginei que existisse uma forma mais simples de fazer e perguntei ao chat como ele faria. Ele me sugeriu a 
seguinte forma de resolução:
'''
# Cria uma matriz 3x3 com todos os elementos inicialmente valendo 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Itera sobre as linhas da matriz
for i in range(3): #Este range evita os três if que eu utilizei no meu código!
    # Itera sobre as colunas da matriz
    for j in range(3):
        # Substitui o valor atual pela entrada do usuário
        matriz[i][j] = int(input(f'Digite o valor para a posição [{i}][{j}]: '))

# Exibe a matriz final
for linha in matriz:
    print(linha)