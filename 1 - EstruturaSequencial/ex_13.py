"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

while True:

    genero = input('Digíte (h) para home e (m) para muler: ')
    altura = input('Digite sua altura para o calculo: ')

    try:
        altura = float(altura)

        if genero == 'h':
            peso = 72.7 * altura - 58
            print(f'Seu peso ideal é {peso:.2f}.')
            break
        elif genero == 'm':
            peso = 62.1 * altura - 44.7
            print(f'Seu peso ideal é {peso:.2f}')
            break
        else:
            print('É preciso digitar o genero e o valor para cálcular o peso.')

    except:
        print('É preciso digítar o valor e o genero para cálcular.')