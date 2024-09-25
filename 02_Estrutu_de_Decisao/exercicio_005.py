
print('-_'*25)
print(' '*17, 'MÉDIA ESCOLAR')
print('-_'*25)
soma_nota = 0

for i in range(1,4):
    nota = float(input(f'Informe sua {i}° nota: '))
    soma_nota += nota
    media = soma_nota/3

if media >= 7:
    print(f'Parabéns você foi APROVADO. Média = {media:.1f}')
elif media < 7:
    print(f'Reprovado! Média atual: {media:.1f}, Abaixo de 7,0')
elif media > 8.5:
    print(f'Parabéns!!! Nota {media:.1f} acima da média')
else:
    print('Algo deu errado, tente novamente.')