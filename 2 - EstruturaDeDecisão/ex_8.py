"""
8 -> Faça um programa que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
while True:
    loja1 = input('Valor da Loja 1: ')
    loja2 = input('Valor da Loja 2: ')
    loja3 = input('Valor da Loja 3: ')

    try:
        loja1 = float(loja1)
        loja2 = float(loja2)
        loja3 = float(loja3)

        if loja1 <= loja2 <= loja3 or loja1 <= loja3 <= loja2:
            print(f'O valor mais barato é da loja 1 R${loja1}')

        elif loja2 <= loja1 <= loja3 or loja2 <= loja3 <= loja1:
            print(f'O valor mais barato é da loja 2 R${loja2}')

        else:
            print(f'O valor mais barato é da loja 3 R${loja3}')
        break

    except:
        print('Valor Invalido!')