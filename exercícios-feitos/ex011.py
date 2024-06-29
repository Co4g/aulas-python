"""
    Um programa que leia a lar e a alt de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m². 
#Código original
l = float(input('Difina a largura da parede em metros: '))
al = float(input('Defina a altura da parede em metros: '))
a = l*al
t = a/2
print('A quantidade de tinta necessária é: ', t, 'litros')
"""
#Versão atualizada
while True:
    print('[]'*20)
    print('ATENÇÃO preencha os dados pedidos em metros.') 
    print('Para casas decimais, utilize pontos no lugar de vírgulas!')
    try:
        lar = float(input('Qual a largura da parede (m)?' ))
        alt = float(input('Qual a altura da parede (m)?' ))
        t = (lar*alt)/2
        break
    except ValueError:
        print('Dados inválidos, por favor, siga corretamente as orientações!')
print('[]'*20)
print(f'Será necessário {t:.2f}l de tinta para pintar toda a parede!')



