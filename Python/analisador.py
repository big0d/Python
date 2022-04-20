mediaidade = 0
somaidade = 0
maioridadeh = 0
nomemaisvelho = ''
mulher20 = 0
for pessoas in range(1, 5):
    print('-=-=-=-=- {}ª PESSOA -=-=-=-=-'.format(pessoas))
    nome = str(input('Insira o nome: ')).strip()
    idade = int(input('Insira a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip()
    somaidade += idade
    if pessoas == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade>maioridadeh:
        maioridadeh = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade<20:
        mulher20 += 1
mediaidade = somaidade/4
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('A media de idade do grupo: {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeh, nomemaisvelho))
print('Das mulheres, {} tem menos de 20 anos'.format(mulher20))
