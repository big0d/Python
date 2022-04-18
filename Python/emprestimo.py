valor = float(input)('Informe o valor da casa: R$ ')
salario = float(input('Informe o seu salario: R$ '))
anos = int(input('Em quantos anos vai pagar pelo emprestimo? '))
prestacao = valor/(anos*12)
minimo = salario*30/100
print('Para comprar uma casa no valor de R$ {:.2f}, a prestacao sera de R$ {:.2f}.'.format(
    valor, prestacao))
if prestacao <= minimo:
    print('O emprestimo foi APROVADO')
else:
    print('O emprestimo foi NEGADO')
