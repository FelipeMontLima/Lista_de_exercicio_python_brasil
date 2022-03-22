"""
7 -> Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

while True:

    base = input('Digite a base do quadrado: ')
    altura = input('Digite a altura do quadrado: ')

    if base.isdigit() and altura.isdigit():

        base = int(base)
        altura = int(altura)

        basexaltura = base * altura
        dobro = basexaltura * 2

        print(f'A área do quadrado é {basexaltura} e seu dobro é {dobro}')
        break

    else:
        if not base.isdigit() and not altura.isdigit():
            print(f'{base} e {altura} não são valores para determinar a área.')
        elif not base.isdigit():
            print(f'{base} não é um valor para determinar a área.')
        elif not altura.isdigit():
            print(f'{altura} não é um valor para determinar a área.')