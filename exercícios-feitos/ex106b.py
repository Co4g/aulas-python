#Forma alterativa sugerida pelo CHAT-GPT para o exercício 106
"""
Nesta forma alternativa, o chat lida com alguns problemas que podem surgir no uso do programa
Além disso, ele lida com o pedido de cores que o professor fez no enunciado e eu ignorei por estar
sem tempo hoje para adicionar cores, usando o módulo colorama, que não mudou muito em relação ao uso
normal de cores.
"""
# Imports
import colorama
from colorama import Fore, Style

# Inicialização do Colorama
colorama.init(autoreset=True)

# Definição de funções
def IHP(funcao):
    print(Fore.CYAN + '-=' * 20)
    print(Fore.YELLOW + f'Manual do comando {funcao}!'.center(40))
    print(Fore.CYAN + '-=' * 20)
    doc = eval(funcao).__doc__
    if doc:
        print(Fore.GREEN + doc)
    else:
        print(Fore.RED + "A função não possui uma docstring.")

# Corpo do Programa
while True:
    comando = input(Fore.BLUE + 'Digite qual função você gostaria de receber o manual: ')
    if comando.upper() == 'FIM':
        break
    else:
        try:
            IHP(comando)
        except Exception as e:
            print(Fore.RED + f"Erro: {e}")

# Finalização do Colorama
colorama.deinit()