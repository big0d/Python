from datetime import date
anoatual = date.today().year
totalmaioridade = 0
totalmenoridade = 0
for pessoas in range(1, 8):
    nasc = int(input('Informe em que ano a {}ª pessoa nasceu: '.format((pessoas))))
    idade = anoatual-nasc
    if idade >= 18:
        totalmaioridade += 1
    else:
        totalmenoridade += 1
print('Nesse grupo, {} pessoas sao maiores de idade e {} menores de idade'.format(totalmaioridade, totalmenoridade))