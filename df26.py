frase = str(input('Escreva uma frase')).strip().upper()
print('A letra A aparece {} vezes na fraze.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} a primeira vez'.format(frase.find('A')+1))
print('A ultiva vez que a letra A apareceu foi na posição {}'.format(frase.rfind('A')+1))