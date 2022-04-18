v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))
v3 = float(input('Insira o terceiro valor: '))
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
elif v3 < v1 and v3 < v2:
    menor = v3
maior = v1
elif v2 > v1 and v2 > v3:
    maior = v2
elif v3 > v1 and v3 > v2:
    maior = v3
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
