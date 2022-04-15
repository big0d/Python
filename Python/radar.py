velocidade = float(input('Informe a velocidade (km/h) em que o carro esta: '))
if velocidade>80:
    print('Voce foi multado por exceder o limite de 80km/h.')
    multa = (velocidade-80)*7 # 7 reais por cada km acima do limite. Vel-80 para multar somente o excesso de velocidade, nao o todo
    print('O valor de sua multa e R$ {:.2f}'.format(multa))
print('Seguranca no transito, uma pauta importante!')