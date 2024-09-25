valor = float(input('Me diga um valor: '))

if valor < 0:
    print(f'O valor é negativo. {valor}')

elif valor > 0:
    print(f'Valor é positivo. {valor}')

else:
    print(f'O valor é zero.')