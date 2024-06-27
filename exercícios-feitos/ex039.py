#Desafio 39 - Alistamento militar
'''
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
Se é a hora de se alistar
Se já passou do tempo do alistamento;
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
print('Você sabe se precisa se alistar? Digite seu ano de nascimento e descubra!')
ano_nas = int(input('Ano de nascimento: '))
alist = 2024 - ano_nas
if alist < 18:
    tem_res = 18 - alist
    print('\033[36mVocê ainda não precisa se alistar!')
    print(f'Ainda faltam {tem_res} anos para você se alistar!\033[m')
elif alist > 18:
    tem_atr = alist - 18
    print(f'\033[31mVocê está {tem_atr} anos atrasado! Procure a junta militar para regularizar sua situação!\033[m')
else: 
    print('\033[32mOlhe que incrível, você está com a idade exata para se alistar. Procura a junta militar assim que possível!\033[m')