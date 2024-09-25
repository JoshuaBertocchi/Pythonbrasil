valor_h = float(input('Quanto você ganhar por hora? '))
horas = int(input('Quantas horas por dia você trabalha? '))
dias = int(input('Quantos dias na semana? '))

calculo_semana= dias*horas

print(f'Na semanha você trabalha {calculo_semana}h.'
      f'\nNa semana você recebe R$:{calculo_semana*valor_h:.2f}'
      f'\nNo mês você recebe: R$:{(calculo_semana*valor_h)*4:.2f}')
