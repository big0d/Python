preco = float(input('Insira o preco do produto? R$ '))
desc = preco - (preco*5/100)

print('Anteriormente por R$ {:.2f}, com desconto esta saindo por R$ {:.2f}}'.format(preco, desc))