valor = input('Digite o que o seu coração mandar: ')
msg = '|| True = verdadeiro // False = falso ||'

print(msg)
print('Tipo primitivo do valor: ', type(valor))
print('Só tem espaços (ao invés de algo digitado)? ', valor.isspace())
print('É um número? ', valor.isnumeric())
print('É alfabético? ', valor.isalpha())
print('É alfanumérico? ', valor.isalnum())
print('Está totalmente em maiúsculas? ', valor.isupper())
print('Está totalmente em minúsculas? ', valor.islower())
print('Está capitalizada? ', valor.istitle())