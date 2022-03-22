import math

while True:
    base = input('Quanto mede a base: ')
    altura = input('Quanto mede a altura: ')

    try:
        base = int(base)
        altura = int(altura)

        area = base * altura
        litros = (area / 6) * 1.1
        latas = math.ceil(litros / 18)
        valor_lata = latas * 80
        galao = math.ceil(litros / 3.6)
        valor_galao = galao * 25

        mixlatas = round(litros / 18)
        mixgaloes = round(litros - mixlatas * 18) * 3.6  # Diferença que sobrou em litros

        if litros - (mixlatas * 18) % 3.6 != 0:
            mixgaloes += 1
            total_mix = (mixlatas * 80) + (mixgaloes * 25)
        print()
        print('=-' * 15)
        print(f'{latas} Latas de 18l R${valor_lata:.2f}')
        print(f'{galao} Galões de 3,6l R${valor_galao}')
        print(f'Mix {mixlatas} latas de 18l e {mixgaloes} galão de 3,6l R${total_mix:.2f}')
        print('=-' * 15)
        print()
    except:
        print()
        print('É preciso dígitar um valor inteiro para o cálculo!')
        print()



