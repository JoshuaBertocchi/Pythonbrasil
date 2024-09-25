peso = float(input('Informe o peso do peixe. KG:'))

if peso < 50:
    print(f'O peso foi a baixo de 50 kg, não deverá pagar multa.')

elif peso >=50:
    diferenca = (peso - 50) * 4
    print(f'O peso passou do limite permitido, deverá pagar R$:{diferenca:.2f} pela diferença.')