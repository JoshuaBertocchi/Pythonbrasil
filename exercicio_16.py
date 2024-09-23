
from math import  ceil
print('-'*50)
print(f'         CALCULO DA QUANTIDADE DE TINTA')
print('-'*50)

base = float(input('Me informe a base (m): '))
altura = float(input('Me informe a altura (m): '))

calculo_area = base * altura
rendimento = calculo_area/3
qtd_latas = ceil(rendimento/18)
valor_pago = qtd_latas * 80

print(f'''01. Sua parede possui {calculo_area:.2f}m²'
02. Será necessário {rendimento:.2f}L de tinta.'
03. N° de Latas de Tintas: {qtd_latas:.2f}
04. Valor Final: R$: {valor_pago:.2f}''')
