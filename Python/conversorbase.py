num = int(input('Insira um numero inteiro: '))
print('''Selecione a base de conversao que deseja:
[1] - Binario
[2] - Octal
[3] - Hexadecimal''')
quero = int(input('Sua opcao: '))
if quero == 1:
    print('{} convertido para binario = {}'.format(num, bin(num)[2:]))
elif quero == 2:
    print('{} convertido para octal = {}'.format(num, oct(num)[2:]))
elif quero == 3:
    print('{} convertido para hexadecimal = {}'.format(num, hex(num)[2:]))
else:
    print('-=! Voce selecionou uma opcao invalida !=-')
