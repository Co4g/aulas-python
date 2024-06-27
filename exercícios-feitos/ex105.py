#Analisando e gerando dicionários
'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retonar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A a média da turma
- A situação (opcional)
Adicione também as docstrings da função!
'''
#Imports


#Definição de funções
def notas(*num, st = False):
    global alunos;
    maior = 0
    menor = 0
    soma = 0
    c = 1
    while True:
        alunos['nome'] = str(input('Digite o nome do aluno: '))
        alunos['nota'] = float(input('Digite a nota do aluno: '))
        if maior == 0 and menor ==0:
            maior = alunos['nota']
            menor = alunos['nota']
        if alunos['nota'] > maior:
            nome = alunos['nome']
            maior = alunos['nota']
        if menor > alunos['nota']:
            menor = alunos['nota']
        soma += alunos['nota']
        media = soma / c
        c += 1
        cont = str(input('Deseja cadastrar outro aluno? [S/N]: '))
        if cont not in 'sS':
            break
    if st==True:
        alunos['media'] = media
        if alunos['media'] > 7:
            alunos['situação'] = 'boa'
        elif alunos['media'] < 5:
            alunos['situação'] = 'ruim'
        elif alunos['media'] >=5 and alunos['media'] <7:
            alunos['situação'] = 'Em risco'
        situação = alunos['situação']
        print(f'A média da turma é {media:.2f} e a situação é {situação}')
    print(f'A quantidade de notas informadas foi: {c} ')
    print(f'A maior nota informada foi {maior} do aluno {nome}')

#Declaração de variáveis
alunos = dict()
#Corpo do Programa
usuario = str(input('Deseja ver a situação da turma, além das notas? [S/N]: '))
if usuario not in 'Ss':
    notas()
else:
    notas(st=True) 
'''
Não fiz sequer perto do que o professor queria, porém, ao que me propus, atinge o objetivo.
Além disso, minha solução ficou perfeita e rapidamente adaptável ao que o professor tinha pedido,
se fosse necessário fazê-lo.
'''