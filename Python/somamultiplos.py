# somar todos os numeros impares multiplos de 3
contador = 0
soma = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        contador += 1
        soma += num
print('A soma dos {} valores: {}'.format(contador, soma))
