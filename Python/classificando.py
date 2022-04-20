from datetime import date
anoatual = date.today().year
nasc = int(input('Informe o seu ano de nascimento: '))
idade = anoatual-nasc
print('O atleta nasceu em {}, portanto tem {} anos em {}.'.format(
    nasc, idade, anoatual))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')
