

while True:
    base = input('Dígite o tamanho da base da área: ')
    altura = input('Digite o tamanho da altura da área: ')

    # Cobertura da Tinta = 3
    # capacidade da lata = 18
    # preço da lata = 80.00

    try:
        base = float(base)
        altura = float(altura)

        area = base * altura
        litros = int(area/3)
        latas_inteiras = int(litros / 18)

        if (litros % 18 != 0):
            latas_inteiras += 1

            valor_total = latas_inteiras * 80.00
            print()
            print('=-' * 15)
            print(f'Área {area:.2f}')
            print(f'Litros de tinta {litros:.2f}')
            print(f'Latas de tintas {latas_inteiras}')
            print(f'Total R${valor_total:.2f}')
            print('=-' * 15)
            break
    except:
        print('É preciso dígitar números para o calculo!')


