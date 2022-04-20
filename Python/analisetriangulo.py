a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))
if a < b + c and b < a+c and c < a+b:
    print('Os segmentos PODEM FORMAR um triangulo')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos NAO PODEM formar um triangulo')
