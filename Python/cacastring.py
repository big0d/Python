# verificar se existe "silva" no nome
nome = str(input('Digite o seu nome COMPLETO: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))