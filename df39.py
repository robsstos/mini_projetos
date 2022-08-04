from datetime import date
atual = date.today().year
nasc = int(input('em qual ano você nasceu?'))
idade = atual - nasc
print('quem naseceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('você tem que se alista esse ano!')
elif idade < 18:
    saldo = 18 - idade
    print('você ainda não tem que 18 anos, faltam {} para você se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade -18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('você deveria ter se alistado em {}'.format(ano))

