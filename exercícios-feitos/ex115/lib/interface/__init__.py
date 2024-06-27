def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
            break
        except (ValueError, TypeError):
            print('Há um erro no dado inserido, por favor, digite um valor inteiro válido! ')
    return n