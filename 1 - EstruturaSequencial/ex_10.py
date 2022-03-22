"""
10 -> Faça um Programa que peça a temperatura em graus Celsius, transforme
e mostre em graus Fahrenheit.
"""

while True:
    c = input('Digite a temperatura em graus Celsius para conversão: ')

    if c.isdigit():
        c = int(c)
        f = c * 1.8 + 32
        print()
        print(f'O valor em graus {c}cº convertido em {f:.2f}fº.')
        break
    else:
        print()
        print('É preciso digitar o valor para conversão.')
        print()