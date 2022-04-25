print('-='*20)
print('        P.A. 10 TERMOS COM WHILE')
print('-='*20)
pt = int(input('> Primeiro termo:  '))
razao = int(input('> Razao:  '))
term = pt
cont = 1
print('-='*20)
while cont <= 10:
    print('{} ➡ '.format(term), end='')
    term += razao
    cont += 1
print('FIM DA PA')
print('-='*20)
