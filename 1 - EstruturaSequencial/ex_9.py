"""
9 -> Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
mostre a temperatura em graus Celsius.
"""

while True:
    f = input('Digite a temperatura em graus Fahrenheit: ')

    if f.isdigit():
        f = int(f)
        c = (f - 32) / 1.8
        print(f'A temperatura em {f}fº convertida para {c:.2f}º.')
        break
    else:
        print('É preciso digitar um valor para conversão.')