real = float(input('Em REAIS, quanto dinheiro você tem na carteira?: R$ '))
dolar = real/4.69
euro = real/5.11
iene = real/0.037
libras = real/6.15

print('-'*10)
print('[13/04/2022 10:00 PM] US$ 1.00 equivale a R$ 4,69')
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))
print('-'*10)
print('[13/04/2022 10:00 PM] € 1.00 equivale a R$ 5,11')
print('Com R$ {:.2f} você pode comprar € {:.2f}'.format(real, euro))
print('-'*10)
print('[13/04/2022 10:00 PM] ¥ 1.00 equivale a R$ 0,037')
print('Com R$ {:.2f} você pode comprar ¥ {:.2f}'.format(real, iene))
print('-'*10)
print('[13/04/2022 10:00 PM] £ 1.00 equivale a R$ 6,15')
print('Com R$ {:.2f} você pode comprar £ {:.2f}'.format(real, libras))
print('-'*10)