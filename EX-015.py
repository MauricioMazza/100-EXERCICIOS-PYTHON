km = float(input('Distancia percorrida em Km:'))
d = int(input('Dias de locação:'))
v = km * .15 + d * 60
print('O valor da locação é de R${:.2f}'.format(v))