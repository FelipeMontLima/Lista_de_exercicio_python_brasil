"""
1 -> Faça um Programa que peça dois números e imprima o maior deles.
"""

while True:
    primeiro_numero = input('Digite o primeiro número: ')
    segundo_numero = input('Digite o segundo número: ')

    try:
        primeiro_numero = float(primeiro_numero)
        segundo_numero = float(segundo_numero)

        if primeiro_numero > segundo_numero:
            print(f'{primeiro_numero} é maior que {segundo_numero}')
        elif segundo_numero > primeiro_numero:
            print(f'{segundo_numero} é maior que {primeiro_numero}')
        else:
            print(f'{primeiro_numero} é igual a {segundo_numero}')
        break

    except:
        print('ERROR!! É preciso dígitar um número!')
