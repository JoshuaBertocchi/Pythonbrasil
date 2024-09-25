print('-_'*25)
print(' '*10, 'Verificador de Vogal')
print('-_'*25)

vogal = 'A', 'E', 'I', 'O' ,'U'

valor = str(input('Digite uma letra: '))

if valor in 'Aa' or valor in 'Ee' or valor in 'Ii' or valor in 'Uu':
    print(f'A letra {valor} é Vogal!')

else:
    print(f'A letra {valor} é Consoante.')