salario = float(input('Informe o seu atual salario: R$ '))
novosalario = salario + (salario*15/100)

print('Seu salario antigo era de R$ {:.2f}, e com reajuste seu novo salario sera de R$ {:.2f}'.format(salario, novosalario))