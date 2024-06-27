#Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Quanto dinheiro você tem na carteira? '))
di = r//3.27
de = r/3.27
ds = r%3.27
print('Você pode comprar exatamente', de, 'dólares com {} reais'.format(r))
print('Você pode comprar', di, 'dólares inteiros com {}'.format(r), 'e restará', ds, 'em reais')
