tamanho_arquivo_MB= float(input('Quantos MB o arquivo possui? '))
velocidade_internet = float(input('Quantos Mega de internet você possui? '))

# Converte a velocidade de Mbps para MBps (1 Mbps = 0,125 MBps)
valocidade_internet_MBps = velocidade_internet * 0.125

tempos_download_segundos = tamanho_arquivo_MB / velocidade_internet
tempos_download_minutos = tempos_download_segundos/60

print(f'O tempo estimado será {tempos_download_minutos:.2f} minutos')
