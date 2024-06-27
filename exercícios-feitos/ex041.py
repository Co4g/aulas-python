#Desafio 41 - Classificando Atletas
'''
A CNN precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''
from datetime import date
import time
print(10*'¬¬¬¬')
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print(10*'¬¬¬¬')
ano_nas = int(input('Digite sua data de nascimento para saber sua categoria: '))
data_atual = date.today()
ano_atual = data_atual.year
cat = ano_atual - ano_nas
print(f'Você tem {cat} ano(s), portanto...')
time.sleep(3)
if cat <= 9:
    print('Sua categoria é Mirim!')
elif cat >= 10 and cat <=14:
    print('Sua categoria é Infantil!')
elif cat >= 15 and cat <=19:
    print('Sua categoria é Junior!')
elif cat == 20:
    print('Sua categoria é Sênior!')
elif cat > 20:
    print('Sua categoria é Master!')

