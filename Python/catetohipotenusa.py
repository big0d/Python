from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
# hip = (co**2+ca**2)**(1/2)
# print('Se o cateto oposto é {} e o cateto adjacente {}, hipotenusa vai medir {:.2f}'.format(co, ca, hip))
hip = hypot(co, ca)
print('Se o cateto oposto é {} e o cateto adjacente {}, hipotenusa vai medir {:.2f}'.format(co, ca, hip))