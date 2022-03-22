"""
7 -> Faça um Programa que leia três números e
mostre o maior e o menor deles.
"""

while True:
    n1 = input('Dígite o primeiro número: ')
    n2 = input('Dígite o segundo número: ')
    n3 = input('Digite o terceiro número: ')

    try:
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)

        if n1 >= n2 >= n3 or n1 >= n3 >= n2:
            if n2 >= n3:
                print(f'Maior Valor {n1}\nMenor Valor {n3}')
            else:
                print(f'Maior Valor{n1}\nMenor Valor {n2}')

        elif n2 >= n1 >= n3 or n2 >= n3 >= n1:
            if n1 >= n3:
                print(f'Maior Valor {n2}\nMenor Valor {n3}')
            else:
                print(f'Maior Valor {n2}\nMenor Valor{n1}')

        else:
            if n2 >= n1:
                print(f'Maior Valor {n3}\nMenor Valor {n1}')
            else:
                print(f'Maior Valor {n3}\nMenor Valor {n2}')

        break

    except:
        print('Erroe, é preciso dígitar um valor!')