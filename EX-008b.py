m = float(input('Digite um valor em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m/10
hm = m/100
km = m/1000
print('Essa distância corresponde a:')
print('{:.0f} mm'.format(mm))
print('{:.0f} cm'.format(cm))
print('{:.0f} dm'.format(dm))
print('{:.0f} m'.format(m))
print('{:.2f} dam'.format(dam))
print('{:.2f} hm'.format(hm))
print('{:.2f} km'.format(km))
