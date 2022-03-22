"""
3 -> Faça um Programa que peça dois números e imprima a soma.
"""

while True:
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')

    if n1.isdigit() and n2.isdigit():
        n1 = int(n1)
        n2 = int(n2)
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} tem a soma {soma}.')
        break
    else:
        if not n1.isdigit() and not n2.isdigit():
            print(f'{n1} e {n2} não são valores para soma!')
        elif not n1.isdigit():
            print(f'{n1} não é um número.')
        elif not n2.isdigit():
            print(f'{n2} não é um valor')
