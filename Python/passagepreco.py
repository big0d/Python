dist = float(input('Qual a distencia da viagem em km?'))
if dist <= 200:
    prec = dist*0.50
else:
    prec = dist*0.45
print('O custo da viagem de {}km fica por {:.2f}'.format(dist, prec))
