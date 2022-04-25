from time import sleep
print('-=-='*10)
print('Ola, bem vindo ao terminal de operacoes')
print('-=-='*10)
sleep(1)
v1 = int(input('Insira o valor 1: '))
v2 = int(input('Insira o valor 2: '))
acao = 0
while acao != 5:
    print('-=-='*10)
    print('''Por favor, solicite uma acao.
    Acoes disponiveis:
    [1] - Somar
    [2] - Multiplicar
    [3] - Saber o maior valor dentre esses
    [4] - Desconsiderar valores e escolher novos numeros
    [5] - Sair do programa''')
    acao = int(input('---> Qual a sua acao?  '))
    if acao == 1:
        soma = v1 + v2
        print('A soma de {} + {} = {}'.format(v1, v2, soma))
    elif acao == 2:
        multiplicacao = v1 * v2
        print('A multiplicacao de {} x {} = {}'.format(v1, v2, multiplicacao))
    elif acao == 3:
        if v1<v2:
            print('O maior valor: {}'.format(v2))
        else:
            print('O maior valor: {}'.format(v1))
    elif acao == 4:
        print('Informe os novos valores...')
        v1 = int(input('Insira o valor 1: '))
        v2 = int(input('Insira o valor 2: '))
    elif acao == 5:
        print('encerrar programa.')
    else:
        print('voce executou uma acao invalida. Tente novamente.')
print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Obrigado por utilizar o nosso terminal!
Volte sempre!''')
