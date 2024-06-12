#Prática da aula 19 sobre dicionários
pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}
#Para referenciar os valores no dicionários, usamos o nome do dicionários, mais sua key entre []:
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos')
for k,v in pessoas.items():
    print(f'{k} = {v}')

#Outro exemplo:
estado = dict()
brasil = list()
for c in range(0, 3):
    estado ['uf'] = str(input('Unidade Federativa: ')) #Declaração a chave UF e pedimos ao usuário seu valor.
    estado['sigla'] = str(input('Sigla do Estado: ')) #Declaração a chave sigla e pedimos ao usuário seu valor.
    brasil.append(estado.copy()) #Para não criar novos dicionários como estado2, estado3, etc, podemos só copiar ele para a lista.
for e in brasil: #percorrerá os três items da lista.
    for v in e.values(): #Percorrerá cada valor dentro do item.
        print(v, end='-')
    print()
