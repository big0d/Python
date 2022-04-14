from math import radians, sin, cos, tan
ang = float(input('Informe o angulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('O angulo {} tem o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, sen, cos, tan))