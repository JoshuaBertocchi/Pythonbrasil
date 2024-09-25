from math import ceil

# Entrada de dados do usuário
base = float(input("Me informe a base/largura (m): "))
altura = float(input("Me informe a altura (m): "))

# Definições de valores
lata = 18
galao = 3.6

# Cálculo da área
area = base * altura

# Acrescentar 10% de folga
area_com_folga = area * 1.1

# Cobertura da tinta
cobertura_por_litro = 6

# Volume das latas e galões
litro_lata = 18
litro_galao = 3.6

# Preços das latas e galões
preco_lata = 80.00
preco_galao = 25.00

# Quantidade total de tinta necessária em litros
litros_necessarios = area_com_folga / cobertura_por_litro

# Situação 1: Apenas latas de 18 litros
latas_necessarias = ceil(litros_necessarios / litro_lata)
preco_apenas_latas = latas_necessarias * preco_lata

# Situação 2: Apenas galões de 3,6 litros
galoes_necessarios = ceil(litros_necessarios / litro_galao)
preco_apenas_galoes = galoes_necessarios * preco_galao

# Situação 3: Misturando latas e galões
latas_misturadas = int(litros_necessarios // litro_lata)
litros_restantes = litros_necessarios % litro_lata
galoes_misturados = ceil(litros_restantes / litro_galao)

preco_misturado = (latas_misturadas * preco_lata) + (galoes_misturados * preco_galao)

# Exibição dos resultados
print("\nSituação 1: Apenas latas de 18 litros")
print(f"Quantidade de latas: {latas_necessarias}")
print(f"Preço total: R$ {preco_apenas_latas:.2f}")

print("\nSituação 2: Apenas galões de 3,6 litros")
print(f"Quantidade de galões: {galoes_necessarios}")
print(f"Preço total: R$ {preco_apenas_galoes:.2f}")

print("\nSituação 3: Misturando latas e galões")
print(f"Quantidade de latas: {latas_misturadas}")
print(f"Quantidade de galões: {galoes_misturados}")
print(f"Preço total: R$ {preco_misturado:.2f}")
