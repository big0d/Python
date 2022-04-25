from random import randint
pc = randint(0,20)
print('-=-='*12)
print('''Bem-vindo ao jogo de adivinhações!!
Pensei em um numero > ENTRE 0 e 20 <
e te desafio a acertar...''')
print('-=-='*12)
acerto = False
palpites = 0
while not acerto:
    jogador = int(input('[?] Qual numero voce acha que é?  '))
    palpites += 1
    if jogador == pc:
        acerto = True
    else:
        if jogador < pc:
            print('[A] Um pouco maior... Tente novamente.')
        else:
            print('[A] Um pouco menor... Tente novamente.')
print('-=-='*12)
print('[R] Bravo! A resposta era {} e Voce acertou depois de {} palpites.'.format(pc, palpites))
print('-=-='*12)
