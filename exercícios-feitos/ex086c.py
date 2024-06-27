#Terceira forma de resolver, sem declarar a matriz com valores zeros
'''
Nas outras duas formas, inicializei a matriz com valores zeros, para ter um referecial.
Neste exemplo, a matriz inicializará com as sublistas (colunas) vazias e será preenchida.
'''
# Declaração de variáveis
matriz = [[], [], []]

# Corpo do programa
for c in range(9):
    valor = int(input('Digite um valor: '))
    if c < 3:
        # Adiciona o valor à primeira sublista
        matriz[0].append(valor)
    elif c < 6:
        # Adiciona o valor à segunda sublista
        matriz[1].append(valor)
    else:
        # Adiciona o valor à terceira sublista
        matriz[2].append(valor)

# Exibe a matriz final
for linha in matriz:
    print(linha)