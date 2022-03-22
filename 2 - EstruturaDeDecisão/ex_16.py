
while True:
    a = input('Digite o valor de a: ')
    b = input('Digite o valor de b: ')
    c = input('Digite o valor de c: ')

    if a == '0':
        print('Isso não é uma conta do segundo grau.')


    else:
        try:
            a = float(a)
            b = float(b)
            c = float(c)

            delta = b ** 2 - 4 * a * c
            if delta < 0:
                print(f'{delta} A equação não possui uma raiz positiva.')
                print('Tente outros valores!')

            # raizes
            x1 = (-b + (delta ** (1 / 2))) / 2 * a
            x2 = (-b - (delta ** (1 / 2))) / 2 * a

            if delta == 0:
                print('A equação possui apenas uma raiz real.')
                print(f'Delta = {delta}')
                print(f'X1 = {x1}')
                print(f'X2 = {x2}')
            elif delta > 0:
                print('A equação possui duas raizes reais.')
                print(f'Delta = {delta}')
                print(f'X1 = {x1}')
                print(f'X2 = {x2}')

        except:
            print('ERROR é preciso digitar números.')