n1 = float(input('Digite a nota da sua primeita avaliação'))
n2 = float(input('Digite a nota da sua segunda avaliaçao'))
m = (n1 + n2)/2
print('A sua media foi {:.2f}'.format(m))
if m >=6.0:
    print('Parabens você foi aprovado')
else:
    print('Bora estudar para a substitutiva')
