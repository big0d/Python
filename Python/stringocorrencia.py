f = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(f.count('A')))
print('A primeira letra A aparece na posicao {}.'.format(f.find('A')+1))
print('A ultima letra A apareceu na posicao {}.'.format(f.rfind('A')+1))