n = str(input('Digite seu nome COMPLETO: ')).upper().strip()
nome = n.split()
print('Seu primeiro nome: {}'.format(nome[0]))
print('Seu ultimo nome: {}'.format(nome[len(nome)-1]))