import random
m = random.randint(0, 5) # o numero que será sorteado
print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. diga qual foi...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei?')) #jogador
if jogador == m:
    print('!!!Parabéns!!! Você acertou!!!')
else:
    print('Você é muito ruim, eu pensei no numero {}, e você digtou {}.'.format(m, jogador))
