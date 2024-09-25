
n_maior = 0
n_menor= 0

for i in range(1,10):
    n = int(input(f'{i}°. Me diga um número: '))

    if i == 1:
        n_maior = n
        n_menor = n
    else:
        if n > n_maior:
            n_maior = n
        if n < n_menor:
            n_menor = n

print(f'Mair número: {n_maior}\nMenor número: {n_menor}')
