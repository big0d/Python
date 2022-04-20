preco = float(input('Insira o preco do produto: '))
escolha = int(input(''''Selecione a forma de pagamento:
[1] A vista dinheiro/cheque
[2] A vista no cartao
[3] Em ate 2x no cartao
[4] 3x ou mais no cartao'''))
if escolha == 1:
    final = preco-(preco*10/100)
    print('Voce tem um desconto de 10%! Com isso, o produto de R$ {:.2f} passa a custar R$ {:.2f}.'.format(preco, final))
elif escolha == 2:
    final = preco-(preco*5/100)
    print('Voce tem desconto de 5%! Com isso, o produto de R$ {:.2f} passa a custar R$ {:.2f}.'.format(preco, final))
elif escolha == 3:
    precoparcela = preco/2
    print('Parcelado em 2x de R$ {:.2f}, o preco de R$ {:.2f} segue o mesmo, sem descontos ou juros.'.format(precoparcela, preco))
elif escolha == 4:
    final = preco+(preco*20/100)
    parcelas = int(input('Quantas parcelas? '))
    precoparcela = final/parcelas
    print('Voce tem juros de 20%. Com isso, o produto de R$ {:.2f} passa a custar R$ {:.2f} atraves de {:.2f} parcelas de R$ {:.2f}.'.format(preco, final, parcelas, precoparcela))
else:
    final = 0
    print('Voce selecionou uma opcao inexistente de pagamento. Por favor, escolha uma valida')
