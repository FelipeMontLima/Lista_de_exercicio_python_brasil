
while True:
    dia = input('Didite o dia: ')
    mes = input('Digite o mês: ')
    ano = input('Digite o ano: ')

    try:

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        print(f'{dia}/{mes}/{ano}')
        break

    except:
        print('ERROR, é preciso dígitar dia, mês e ano')
