"""
18 -> Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).

---Cálculo---
Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos
Um arquivo de 15 MB, baixado a 10 Mb/s: 15 / (10/8) = 12 segundos.
"""

while True:
    mb = input('Digite o tamanho do arquivo em MB: ')
    mbps = input('Digite a velocidade da internet em Mbps: ')

    try:
        mb = int(mb)
        mbps = int(mbps)
        tempo_segundos = (mb / (mbps / 8))

        print()
        print('=-' * 10)
        print(f'Arquivo {mb} MB\n'
              f'Velocidade {mbps} Mbps\n'
              f'Tempo {tempo_segundos:.2f} segundos')
        print('=-' * 10)
        print()
        break

    except:
        print()
        print('*' * 52)
        print('É preciso digitar um valor para o tempo de download!')
        print('*' * 52)
        print()


