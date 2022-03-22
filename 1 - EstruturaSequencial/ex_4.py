"""
4 -> Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""



while True:
    print('Digite as 4 notas do aluno!')
    n1 = input('Digite a primeira nota: ')
    n2 = input('Digite a segunda nota: ')
    n3 = input('Digite a terceira nota: ')
    n4 = input('Digite a quarta nota: ')

    if n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit():
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4)
        media = (n1 + n2 + n3 + n4) / 2

        print(f'A média do aluno é {media}.')
        break

    else:
        if not n1.isdigit() and not n2.isdigit() and not n3.isdigit() and not n4.isdigit():
            print('Você não digitou nenhum valor para média. Tente de novo')

            #Com três valores
        elif not n1.isdigit() and not n2.isdigit() and not n3.isdigit():
            print(f'{n1}, {n2} e {n3} não são valores para média.')
        elif not n1.isdigit() and not n2.isdigit() and not n4.isdigit():
            print(f'{n1}, {n2}, {n4} não sao valores para média.')
        elif not n1.isdigit() and not n3.isdigit() and not n4.isdigit():
            print(f'{n1}, {n3} e {n4} não são valores para média.')
        elif not n2.isdigit() and not n3.isdigit() and not n4.isdigit():
            print(f'{n2}, {n3} e {n4} não são valores para média.')

            #com dois valores
        elif not n1.isdigit() and not n2.isdigit():
            print(f'{n1} e {n2} não são valores para média.')
        elif not n1.isdigit() and not n3.isdigit():
            print(f'{n1} e {n3} não são valores para média.')
        elif not n1.isdigit() and not n4.isdigit():
            print(f'{n1} e {n4} não são valores para média.')
        elif not n2.isdigit() and not n3.isdigit():
            print(f'{n2} e {n3} não são valores para média.')
        elif not n2.isdigit() and not n4.isdigit():
            print(f'{n2} e {n4} não são valores para média.')
        elif not n3.isdigit() and not n4.isdigit():
            print(f'{n3} e {n4} não são valores para média.')

            #com um valor
        elif not n1.isdigit():
            print(f'{n1} não é um valor para média.')
        elif not n2.isdigit():
            print(f'{n2} não é um valor para média.')
        elif not n3.isdigit():
            print(f'{n3} não é um valor ára média.')
        elif not n4.isdigit():
            print(f'{n4} não é valor para média.')
