
ano = input('Digite o ano: ')

if ano.isdigit():

    ano = int(ano)
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto!')

else:
    print('ERROR, é preciso digitar um ano.')
