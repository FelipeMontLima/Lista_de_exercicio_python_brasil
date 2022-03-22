"""
6 -> Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

cálculo -> área = pi * raio ** 2
"""

import math

pi = math.pi

while True:

    r = input('Digite o valor do RAIO: ')

    if r.isdigit():
        r = int(r)
        area = pi * r ** 2
        print(f'O valor da area é {area:.2f}.')
        break
    else:
        if not r.isdigit():
            print(f'{r} não é um valor para calcular a área')
