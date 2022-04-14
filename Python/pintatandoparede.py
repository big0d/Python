larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg*alt
tinta = area/2

print('Sua parede tem a dimensão de {}X{} e sua área de {}m²'.format(larg, alt, area))
print('Para pintar essa parede, voce precisara de {}l de tinta'.format(tinta))