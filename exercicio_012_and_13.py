
sexo = str(input('Me informe sua sexualidade (masculino/feminino): ')).lower()

if sexo == 'feminino' or sexo == 'feminina':
    altura = float(input('Me informe sua altura (ex: 1.70): '))
    peso_ideal = ((62.1 * altura) - 44.7) #00. IMC FEMININO
    print(f'IMC Feminino {peso_ideal:.2f} KG')

elif sexo == 'masculino':
    altura = float(input('Me informe sua altura (ex: 1.70): '))
    peso_ideal = ((72.7 * altura) - 58)  # 00. IMC MASCULINO
    print(f'Seu peso ideal é: {peso_ideal:.2f} KG')

else:
    print('Algo deu errado, tente novamente.')


