print('\033[34m-='*20)
print('\033[31m         SEQUENCIA DE FIBONACCI')
print('\033[34m-='*20)
print('''\033[33mNa matemática, a sucessão de Fibonacci
é uma sequência de números inteiros, começando
normalmente por 0 e 1, na qual cada termo
subsequente corresponde à soma dos dois 
anteriores.''')
print('\033[34m-='*20)
num = int(input('\033[m> Quantos termos tera a sequencia?  '))
term1 = 0
term2 = 1
print('{} ➡ {}'.format(term1, term2), end='')
cont = 3
while cont <= num:
    term3 = term1+term2
    print(' ➡ {}'.format(term3), end='')
    term1 = term2
    term2 = term3
    cont += 1
print(' ➡ FIM')
print('\033[34m-='*20)
