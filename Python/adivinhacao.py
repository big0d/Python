from random import randint
pc = randint(0, 10) # comando q sorteia o numero que o pc ira escolher
print('-=--=-'*12)
print('Com minha inteligente suprema, estou pensando em um numero entre 0 e 10... adivinhe se puder!')
print('-=--=-'*12)
player = int(input('Em que numero eu pensei? ')) # ler a resposta de quem esta jogando
if player == pc:
    print('De fato brilhante! Voce conseguiu adivinhar.')
else: 
    print('HAHAHA! Voce foi superado pela minha inteligencia. \n O numero pensado foi {}, enquanto voce apostou no {} e perdeu.'.format(pc, player))