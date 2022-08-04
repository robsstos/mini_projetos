casa = float(input('Qual o valor do imovel que você vai financiar?: R$'))
salario = float(input('Qual o valor do seu salario?: R$'))
tempo = int(input('Em quantos anos deseja financiar?'))
prestação = casa / (tempo * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, tempo), end='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Seu financiamento foi aprovado')
else:
    print('No momento seu emprestimo foi negado!')
print('Obrigado')