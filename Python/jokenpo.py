from random import randint
from time import sleep
acoes = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(1, 3)
print('-='*15)
print('''Escolha sua jogada:
[1] Pedra
[2] Papel
[3] Tesoura''')
escolha = int(input('Qual voce escolhe?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*15)
print('O computador escolheu... {}'.format(acoes[pc]))
print('O jogador escolheu {}!'.format(acoes[escolha]))
print('-='*15)
if pc == 1:  # PEDRA
    if escolha == 1:
        print('Houve um empate. Finalmente um oponente a altura!')
    elif escolha == 2:
        print('VENCEU! O jogador derrotou o computador.')
    elif escolha == 3:
        print('PERDEU! O computador superou o jogador.')
    else:
        print('!! Voce escolheu uma jogada invalida !!')
elif pc == 2:  # PAPEL
    if escolha == 1:
        print('PERDEU! O computador superou o jogador.')
    elif escolha == 2:
        print('Houve um empate. Finalmente um oponente a altura!')
    elif escolha == 3:
        print('VENCEU! O jogador derrotou o computador.')
    else:
        print('!! Voce escolheu uma jogada invalida !!')
elif pc == 3:  # TESOURA
    if escolha == 1:
        print('VENCEU! O jogador derrotou o computador.')
    elif escolha == 2:
        print('PERDEU! O computador superou o jogador.')
    elif escolha == 3:
        print('Houve um empate. Finalmente um oponente a altura!')
    else:
        print('!! Voce escolheu uma jogada invalida !!')
