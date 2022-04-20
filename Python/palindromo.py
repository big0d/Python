print('-=-=-=-=- PALINDROMO -=-=-=-=-')
frase = str(input('Digite uma frase: ')).strip().upper()
p = frase.split()
j = ''.join(p)
i = j[::-1]
print(j,' -> ', i)
if i == j:
    print('E um palindromo')
else:
    print('Nao e um palindromo')
