v = float(input('Qual sua velocidade?'))
if v > 80:
    print('Você foi multado por exesso de velocidade. O limite da via é 80Km/h')
    multa = (v-80) * 7
    print('Você foi multado em R${:.2f}!'.format(multa))
print('Dirija com cuidado. tenha um bom dia')