num = int(input('Digite um numero inteir!'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('sua opção:'))
if opção == 1:
    print('{} Convertido para BINARIO é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção invalida!')