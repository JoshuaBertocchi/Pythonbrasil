
from math import pow
n_01 = int(input('Me diga um número: '))
n_02 = int(input('Me diga mais um número: '))
n_03 = float(input('Me diga um número real: '))

calculo_01 = (n_01 * 2) * (n_02/2)
calculo_02 = (n_01 * 3) + n_03
calculo_03 = pow(n_03, 3)

print(f'01. O produto do dobro do primeiro com metade do segundo.'
      f'\nResposta:{calculo_01:.2f}')
print(f'02. A soma do triplo do primeiro com o terceiro.'
      f'\nResposta: {calculo_02:.2f}')
print(f'03. O terceiro elevado ao cubo.'
      f'\nResposta:{calculo_03:.2f}')