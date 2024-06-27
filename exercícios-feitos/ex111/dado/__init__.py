#Função dado

def leiadinheiro (valor):
    while True:
        entrada = str(input(valor)).replace(',', '.').strip()
        if entrada.isalpha() or entrada== '':
            print(f'ERRO:  {entrada} é um preço inválido!')
        else:
            break
    return float(entrada)

