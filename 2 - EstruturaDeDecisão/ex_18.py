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

        print(f'{dia}/{mes}/{ano}')
        break

    except:
        print('ERROR, é preciso dígitar dia, mês e ano')
