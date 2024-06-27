"""
    Um programa que leia a lar e a alt de uma parede em metros, calcule a sua área e a quantidade
de tinata necessária para pintá-la, sabendo que cada litro de tinta pinta uma parea de 2m². 
"""
l = float(input('Difina a largura da parede em metros: '))
al = float(input('Defina a altura da parede em metros: '))
a = l*al
t = a/2
print('A quantidade de tinta necessária é: ', t, 'litros')
