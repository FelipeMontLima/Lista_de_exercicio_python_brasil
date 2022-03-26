"""
18 - > Faça um Programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida.
"""
while True:
    dia = input('Didite o dia: ')
    mes = input('Digite o mês: ')
    ano = input('Digite o ano: ')

    try:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if dia > 0 and mes > 0 and ano > 0:
            if dia < 10 and mes < 10:
                print(f'0{dia}/0{mes}/{ano}')
            elif dia < 10:
                print(f'0{dia}/{mes}/{ano}')
            elif mes < 10:
                print(f'{dia}/0{mes}/{ano}')
            else:
                print(f'{dia}/{mes}/{ano}')

        else:
            print('Zero não é uma data!')

    except:
        print('ERROR, é preciso dígitar dia, mês e ano')
