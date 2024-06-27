#Desafio 73 - Tupla com Times de Futebol
'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro, na ordem de colocação.
Depois mostre:
1 - Apenas os 5 primeiros colocados.
2 - Os últimos 4 colocados.
3 - Uma lista com os times em ordem alfabética.
4 - Em que posição na tabela está o time da Chapecoense (por questões de atualização, substituirei a Chape pelo criciúma).
'''
#Tabela do campeonato brasileiro de futebol masculino dia 07/06/2024 às 18:03. Fonte: Google
tabela = ("Cheirinho", "Botafogo da Bahia", "Garrincha FC", "São Bis", "Tapetinho-PR", "Energético Estragado", 
          "Tapetinho-SP", "Coloridas", "Bolacha", "Pintinho", "Vice da LDU", "Grama de Neve", "Grêmio maior de todos", 
          "Vasco kkkkkkkkk", "FluminenCe", "Criciúma pequeno demais pra zoar", "Time do Faz o L", "Menor dos Atlético", 
          "GP FC", "Time do Deyverson")
print(f'Os cinco primeiros colocados são: {tabela [0:5]}')
print('#'*25)
print(f'Os atuais times da zona de rebaixamento são: {tabela [16:20]}') #Ou tabela[-4:]
print('#'*25)
print(sorted(tabela))
#Adicionei 1 ao index para refletir a posição real do criciúma. Nâo sabia como fazê-lo, então consultei o Chat-GPT, que me sugeriu essa solução!
print(f'O criciúma se encontra na posição {tabela.index('Criciúma pequeno demais pra zoar') + 1}')