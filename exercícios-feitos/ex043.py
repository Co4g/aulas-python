#Desafio 43 - índice de Massa corporal
'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do Peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
30 até 40: Obesidade
- Acima de 40: Obesidade mórbida.
'''
print(20*'\033[31m|||')
print('Cálculadora de IMC, descubra se você está gordo ou não!')
print(20*'|||')
alt = float(input('Digite sua altura em metros sem a unidade de medida. Ex: 1.72 '))
peso = float(input('Digite seu peso em quilos sem a unidade de medida. Ex: 70 '))
imc = peso / alt**2
print(f'Seu imc é: {imc:.2f}!')
if imc < 18.5:
    print('Você está abaixo do peso magrelo!')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está no seu peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está um pouco acima do peso, cuidado para não ficar obeso!')
elif imc >=30 and imc <40:
    print('Você está obeso, vai emagrecer seu gorducho!')
else:
    print('Tá quase morrendo já! Liga pro médico, porque se tu tentar ir a pé, seu coração para!') 