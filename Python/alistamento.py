from datetime import date
anoatual = date.today().year
nasc = int(input('Informe seu ano de nascimento em QUATRO digitos: '))
idade = anoatual-nasc
print('Se voce nasceu em {}, atualmente em {} voce tem {} e'.format(
    nasc, anoatual, idade))
if idade == 18:
    print('voce precisa se alistar o mais rapido possivel')
elif idade < 18:
    falta = 18-idade
    print('voce ainda nao precisa se alistar. Faltam {} anos.'.format(falta))
    anoalistamento = anoatual+falta
    print('seu alistamento sera em {}'.format(anoalistamento))
elif idade > 18:
    falta = idade-18
    print('voce deveria ter se alistado ha {} anos'.format(falta))
    anoalistamento = anoatual-falta
    print('seu alistamento foi em {}'.format(anoalistamento))
elif idade > 100:
    print('ta fazendo hora extra hein irmao')
