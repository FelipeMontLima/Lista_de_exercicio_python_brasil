"""
11 -> Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

while True:

    n1 = input('Digíte o primeiro valor inteiro: ')
    n2 = input('Digite o segundo valor inteiro: ')
    n3 = input('Digite o terceiro valor Real: ')

    try:
        n1 = int(n1)
        n2 = int(n2)
        n3 = float(n3)

        dobro = n1 * 2
        metade = n2 / 2
        triplo = n1 * 3 + n3
        cubo = n3 ** 3

        print(f'O dobro de {n1} é {dobro} e a metade de {n2} é {metade}.')
        print(f'O triplo de {n1} somado pelo {n3} é {triplo}.')
        print(f'O valor {n3} elevado ao cubo é {cubo:.2f}.')
        break

    except:
        print()
        print('É preciso colocar um valor para os devidos cálculos.')
        print()

