#Desafio 44 - Gerenciador de Pagamentos
'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartao: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
print('Olá, sou seu assistente de pagamento, vamos começar?')
valor = float(input('Vamos começar adicionando o valor do produto que você deseja comprar: R$ '))
form = str(input('Agora defina a forma de pagamento:\n'
                '1 - À vista dinheiro/cheque(10% de desconto)\n'
                '2 - À vista no cartão (5% de desconto!)\n'
                '3 - 2x no cartão\n'
                '4 - 3x ou mais no cartão(20% juros)!\n'))
if form == '1':
    desconto = (valor*10) / 100
    val_fin = valor - desconto
    print(f'Seu desconto será de R${desconto:.2f} e o valor final ficará R${val_fin:.2f}!')
elif form == '2':
    desconto = (valor*5) / 100
    val_fin = valor - desconto
    print(f'Seu desconto será de R${desconto:.2f} e o valor final ficará R${val_fin:.2f}!')
elif form == '4':
    juros = (valor*20) / 100
    val_fin = valor + juros
    print(f'Você pagará R${juros:.2f} de juros e o valor final ficará R${val_fin:.2f}')
elif form == '3':
    print('Com esta forma de pagamento, o valor permanecerá o mesmo!')
else:
    print('Por favor, digite uma opção válida!')