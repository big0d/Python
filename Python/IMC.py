peso = float(input('Informe o seu peso (Kg): '))
alt = float(input('Informa a sua altura (m): '))
imc = peso/(alt**2)
print('Com peso de {}Kgs e altura de {}m, o IMC e {:.1f}'.format(peso, alt, imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO.')
elif imc >= 18.5 and imc < 25:
    print('Voce esta no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Voce esta com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Voce esta com OBESIDADE')
else:
    print('Voce esta com OBESIDADE MORBIDA')
