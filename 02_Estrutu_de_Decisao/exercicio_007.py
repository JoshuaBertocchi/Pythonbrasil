
for i in range(1,4):
    n = int(input(f'{i}°.Digite um número: '))

    if i == 1:
        maior_n= n
        menor_n= n
    else:
        if n > maior_n:
            maior_n = n
        if n < menor_n:
            menor_n = n
print(f'O Maior número é {maior_n}.')
print(f'O Menor número é {menor_n}.')