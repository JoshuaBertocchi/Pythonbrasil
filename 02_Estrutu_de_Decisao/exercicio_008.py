

for o in range(1,4):
    produto_valor = float(input(f'{o}. Me diga o valor do produto? R$ '))

    if o == 1:
        menor_valor = produto_valor


    if produto_valor < menor_valor:
        menor_valor = produto_valor

print(f'O valor mais barato é R$:{menor_valor:.2f}. Indicamos essa para ser comprada!')