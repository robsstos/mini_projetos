resp = 'S'
soma = quant = média =0
while resp in 'Ss':
    núm = int(input('digite um numero: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
média = soma / quant
print('você digitou {} números e a media foi {}'.format(quant, média))
print('O maior valor foi {} o menor foi{} '.format(maior, menor))