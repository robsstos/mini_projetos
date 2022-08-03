nome = str(input('Escreva seu nome completo!')).strip()
print('Seu nome em letras maiusculas é {}.'.format(nome.upper()))
print('Seu nome em letras minusculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

