"""
6 -> Faça um Programa que leia três
números e mostre o maior deles.
"""
while True:
    n1 = input('Dígite o primeiro valor: ')
    n2 = input('Dígite o segundo valor: ')
    n3 = input('Dígite o terceiro valor: ')

    try:
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)

        print(f'Primero Valor {n1}\nSegundo Valor {n2}\nTerceiro Valor {n3}')

        if n1 >= n2 >= n3 or n1 >= n3 >= n2:
            print(f'O maior número é {n1}')
        elif n2 >= n1 >= n3 or n2 >= n3 >= n1:
            print(f'O maior número é {n2}')
        else:
            print(f'O maior número é {n3}')
        break

    except:
        print('Error, é preciso dígitar um valor: ')