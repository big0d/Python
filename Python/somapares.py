# ler seis numeros inteiros e mostrar a soma dos que q forem pares
somar = 0
contar = 0
for v in range(1, 7):
    num = int(input('Insira o valor n{} : '.format(v)))
    if num % 2 == 0:
        somar += num
        contar += 1
print('Com {} numeros PARES informados, a soma foi {}'.format(contar, somar))
