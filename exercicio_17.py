from math import ceil
from time import sleep

base = float(input('Me informe a base/largura (m): '))
altura = float(input('Me informe a Altura (m): '))

lata = 18
galao = 3.6
lata_valor = 80
galao_valor = 25
calculo_area = base * altura
rendimento_tinta = (calculo_area/6) * 1.1
#acrescimento10 = rendimento_tinta + (rendimento_tinta * 1.1)


qtd_latas_18l = ceil(rendimento_tinta/lata)
valor_final_lata_18l = qtd_latas_18l * lata_valor
qtd_latas_3_6l = ceil(rendimento_tinta/galao)
valor_final_lata_3_6l = qtd_latas_3_6l * galao_valor

latas_misturadas18 = int(rendimento_tinta//lata)
latas_restantes18 = rendimento_tinta % lata
galoes_misturados = ceil(latas_restantes18 / galao)
valor_final_mistura = (latas_misturadas18 * lata_valor) + (galoes_misturados * galao_valor)

print('-'*30)
print('           Calculo')
print('-'*30)
print(f'''01. Área a ser pintada: {calculo_area:.2f} m².

02.Comprando apenas galões de 3,6L(Qtd:{qtd_latas_3_6l}). 
- Valor Final: R$: {valor_final_lata_3_6l:.2f}

03.Comprando apenas latas de 18L(Qtd:{qtd_latas_18l}).
- Valor Final: R$: {valor_final_lata_18l:.2f}

04.Contagem misturada:
- Quantidade Latas: {latas_misturadas18}
- Quantidade Galões: {galoes_misturados}
- Valor Final: R$ {valor_final_mistura}
''')
