largura=float(input('largura da parede: '))
altura=float(input('altura da parede: '))
area=largura*altura
print('sua parede tem dimensão de {} x {} e sua area é de {} metros quadrados'.format(largura,altura,area))
tinta=area/2
print('para pintar essa parede voce precisa de {} litros de tinta'.format(tinta))