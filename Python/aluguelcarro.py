dias = int(input('Quantos dias alugados? '))
qkm = float(input('Quantos Km percorridos pelo carro? '))
preco = (dias*60)+(qkm*0.15)

print('Total a pagar: R$ {:.2f}'.format(preco))