print('-='*33)
print('Programa que prossiga somente se vc digitar corretamente no campo')
print('-='*33)
genero = str(input('Informe seu genero [M/F]:  ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Dados invalidos, tente novamente. Informe seu genero [M/F]:  ')).strip().upper()[0]
print('Confirmacao - genero: {}'.format(genero))
idade = int(input('Informe sua idade: '))
print('Confirmacao - idade: {}'.format(idade))
