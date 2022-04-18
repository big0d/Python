from datetime import date
ano = int(input('Informe o no que quer analisar ou digite 1 para analisar o ano atual: '))
if ano == 1:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} nao é bissexto.'.format(ano))