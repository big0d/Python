print('-='*20)
print('        P.A. 10 TERMOS COM WHILE')
print('-='*20)
pt = int(input('> Primeiro termo:  '))
razao = int(input('> Razao:  '))
term = pt
cont = 1
tt = 0
extras = 10
print('-='*20)
while extras != 0:
    tt = tt + extras
    while cont <= tt:
        print('{} ➡ '.format(term), end='')
        term += razao
        cont += 1
    print('FIM')
    print('-=' * 20)
    extras = int(input('Quantos termos extras voce quer mostrar?  '))
print('-=' * 20)
print('''> !! FIM DA EXECUCAO DO PROGRAMA !! <
No total, {} termos foram mostrados.'''.format(tt))
print('-=' * 20)
