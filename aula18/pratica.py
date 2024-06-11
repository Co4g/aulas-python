#Pratica da aula 18

#Declaração de variáveis:
galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: '))) #Lê o nome digitado e adiciona a lista dado.
    dado.append(int(input('Idade: '))) #Lê a idade digitada e adiciona a lista dado.
    galera.append(dado[:]) #Adiciona a lista dado inteira a lista galera.
    dado.clear() #Limpa a lista dado, para que ela não acumule elementos e repita-os quando o loop rodar novamente.

for p in galera:
    if p[1] >= 18: #Verifica o elemento 1 da sublista, que nesse caso é a idade, para ver se é adulto ou não.
        print(f'{p[0]} é maior de idade.') #Se for adulto, printa o elemento zero da sublista, que é o nome!
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.') 
        totmen += 1
        print(f'Temos {totmai} maiores e {totmen} menores de idade.')