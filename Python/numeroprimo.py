num = int(input('Insira um numero: '))
total = 0
print('''-=-=-=-=-=-=-=-=-=-=-=-=-
Azul: divisivel
Vermelho: nao divisivel
-=-=-=-=-=-=-=-=-=-=-=-=-''')
for c in range(1, num+1):
    if num%c==0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('Ele é um NUMERO PRIMO')
else:
    print('Ele NAO E um numero primo')