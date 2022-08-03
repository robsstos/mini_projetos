distancia = float(input('Quantos km tem sua viagem?'))
if distancia <=200:
    da = distancia * .50
    print('Sua passagem vai custa R${:.2f}.'.format(da))
else:
    db = distancia * .45
    print('Sua passagem vai custa R${:.2F}.'.format(db))
