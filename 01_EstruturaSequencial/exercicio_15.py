valor_hora = float(input('Quanto você receber por hora? '))
qtd_hora = float(input('Quantas horas você trabalha? '))
dias = int(input('Quantos dias na semana você trabalha? '))


salario_bruto = (valor_hora * qtd_hora) * (dias * 4)

taxa_ir = (salario_bruto * 11)/100   #* Taxa IR(11%)
taxa_inss = (salario_bruto * 8 )/100 #* Taxa INSS(8%)
taxa_sindicato= (salario_bruto * 5)/100 #* Taxa Sindicato(5%)
taxa_total = taxa_ir + taxa_inss + taxa_sindicato  #* Taxa valor total

salario_taxado = salario_bruto - taxa_total

print(f'Salário Bruto: R${salario_bruto:.2f}'
      f'\nTaxa IR(11%): R$ {taxa_ir:.2f}'
      f'\nTaxa INSS(8%): R$ {taxa_inss:.2f}'
      f'\nTaxa Sindicato(5%): R$ {taxa_sindicato:.2f}'
      f'\nSalário Liquido: R$ {salario_taxado:.2f}')
