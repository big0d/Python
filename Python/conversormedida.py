medida = float(input('Insira uma distância em metros: '))
cm = medida*100
mm = medida*1000
dm = medida * 10
dam = medida/10
hm = medida/100
km = medida/1000
msg = 'km, hm, dam, m, dm, cm, mm'
print(msg)
print('a medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))