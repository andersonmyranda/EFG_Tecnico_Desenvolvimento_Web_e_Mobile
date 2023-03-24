idade = int(input('Qual sua idade?'))

if idade >= 18:
    print('Você é maior de idade com {} anos.'.format(idade), 'Parabéns!!')

elif idade <= 12:
    print('Você é uma criança com idade de {} anos'.format(idade))

elif idade <= 15:
    print('Você é um adolescente  com idade de {} anos'.format(idade))

else:
    print('Você é menor de idade com  {} anos.'.format(idade), 'Sinto muito!')
