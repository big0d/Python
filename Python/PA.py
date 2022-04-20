first = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimotermo = first+(10-1)*razao
for c in range(first, decimotermo+razao, razao):
    print('{} '.format(c), end='-> ')
print('-=-=- FIM -=-=-')
