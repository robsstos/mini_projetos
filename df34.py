salario = float(input('Qual é seu salario'))
if salario > 1250.00:
    novo = salario * 1.10
else:
    novo = salario * 1.15
print('Seu novo salario apos o almento é RS {:.2F}'.format(novo))
