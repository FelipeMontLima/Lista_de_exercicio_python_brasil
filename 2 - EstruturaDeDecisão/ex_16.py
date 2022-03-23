"""
16 -> Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
e fazer as consistências, informando ao usuário nas seguintes situações:

a - Se o usuário informar o valor de A igual a zero, a equação não é do
segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

b - Se o delta calculado for negativo, a equação não possui raizes
reais. Informe ao usuário e encerre o programa;

c - Se o delta calculado for igual a zero a equação possui apenas uma raiz
real; informe-a ao usuário;

d - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
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