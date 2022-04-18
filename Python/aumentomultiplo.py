salario = float(input('Qual e o salario do funcionario? R$ '))
if salario <= 1250:
    aumento = (salario*15/100)+salario
else:
    aumento = (salario*10/150)+salario
print('O salario antigo de R$ {:.2f} com aumento ficou por R${:.2f}'.format(salario, aumento))
