"""
5 -> Faça um Programa que converta metros para centímetros.
"""

while True:
    m = input('Digite o valor em metros: ')
    if m.isdigit():
        m = int(m)
        cm = m * 100
        print(f'{m}m convertido para centimetros {cm}cm.')
        break
    else:
        if not m.isdigit():
            print(f'{m} não é um valor para conversão.')