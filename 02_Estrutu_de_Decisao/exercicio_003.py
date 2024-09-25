sexo = str(input('Me informe seu sexo (F/M): '))

if sexo in 'Mn':
    print('Sexo Masculino.')
elif sexo in 'Ff':
    print('Sexo Feminino.')
else:
    print('Sexo inválido.')