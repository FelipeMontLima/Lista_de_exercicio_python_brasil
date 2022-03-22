"""
9 -> Faça um Programa que leia três números e
mostre-os em ordem decrescente.
"""

while True:

    n1 = input('Dígite o primeiro número: ')
    n2 = input('Dígite o segundo número: ')
    n3 = input('Dígite o terceiro número: ')

    try:
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)

        if n1 >= n2 >= n3:
            print(f'{n1}, {n2}, {n3}')
        elif n1 >= n3 >= n2:
            print(f'{n1}, {n3}, {n2}')
        elif n2 >= n1 >= n3:
            print(f'{n2}, {n1}, {n3}')
        elif n2 >= n3 >= n1:
            print(f'{n2}, {n3}, {n1}')
        elif n3 >= n1 >= n2:
            print(f'{n3}, {n1}, {n2}')
        elif n3 >= n2 >= n1:
            print(f'{n3}, {n2}, {n1}')

    except:
        print('Erroe, é preciso dígitar um número!')