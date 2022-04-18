pn = float(print('Insira a primeira nota: '))
sn = float(print('Insira a segunda nota: '))
media = (pn+sn)/2
print('Com notas {:.1f} e {:.1f}, o aluno tera media de {:.1f}.'.format(pn, sn, media))
if media < 5:
    print('REPROVADO filhao')
elif media >= 5 and media<7:
    print('RECUPERACAO meu faixa')
else:
    print('APROVADO parabens')
