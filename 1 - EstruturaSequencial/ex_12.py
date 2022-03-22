"""
12 -> Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule
seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

while True:

    h = input('Digíte sua altura: ')

    try:
        h = float(h)

        peso = 72.7 * h - 58

        print(f'Seu peso ideal é {peso:.2f}.')
        break
    except:
        print('É preciso digítar sua altura para o calculo!')