"""
2 -> Faça um Programa que peça um valor e mostre na tela se o valor
é positivo ou negativo.
"""

while True:

    numero = input('Dígite um número para ver se é Positivo ou Negativo: ')

    try:
        numero = float(numero)

        if numero >= 0:
            print(f'{numero} é POSITIVO!')
        else:
            print(f'{numero} é NEGATIVO!')
        break
    except:
        print('É preciso digitar um número para comparação!')