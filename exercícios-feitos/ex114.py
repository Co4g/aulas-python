#Desafio 114 - Site está acessivel?
'''
Crie um código em Python que teste se o site pudim está acessivel pelo computador usado.
'''
import requests
def verifica_site(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f'O site {url} está acessível!')
        else:
            print(f'O site {url} retornou o status code {response.status_code}.')
    except requests.exceptions.RequestException as erro:
        print(f'O site {url} está inacessível. Erro: {erro}')


verifica_site("https://www.pudim.com.br")
'''
Fiz de um jeito próprio e não funcionou na hora de colocar a url. Pensei ter feito errado e, desistindo, pedi ao Chat-GPT uma solução. A dele era próxima da minha, porém um pouco maior e mais complexa. Então, escrevi o código que ele sugeriu e ainda deu erro. No fim, percebi que faltava o protocolo http// na hora de colocar a url e que, na verdade, meu primeiro código provavelmente estava funcional e mais simples. Mas acabei deixando a solução sugerida pelo Chat por entender que não há perda nenhuma nisso.
'''