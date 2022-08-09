from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue acertar?')
acertou = False
chute = 0
while not acertou:
    jogador = int(input('Qual é o seu chute? '))
    chute += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais!!! ')
        elif jogador > computador:
            print('Um pouco menos!!! ')
print('Parabéns você precisou de {} tentativas. '.format(chute))
