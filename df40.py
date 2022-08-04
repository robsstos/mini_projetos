nota1 = float(input('qual sua primeira nota?'))
nota2 = float(input('qual sua segunda nota?'))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Parabens sua media foi {:.2f} você foi aprovado'.format(media))
elif media < 5:
    print(' sua meida foi {:.2f}, você foi reprovado'.format(media))
elif media >= 5 and media < 7:
    print('suma sua media foi {} você está de recuperação'.format(media))
