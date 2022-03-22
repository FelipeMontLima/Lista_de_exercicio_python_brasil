"""
4 -> Faça um Programa que verifique se uma letra
digitada é vogal ou consoante.
"""

while True:

    letra = input('Digite uma letra: ')

    vogal = 'aeiou'

    consoante = 'bcçdfghjklmnpqrstvwxyz'

    if letra in vogal or letra in vogal.upper():
        print(f'{letra} é uma vogal!')
        break
    elif letra in consoante or letra in consoante.upper():
        print(f'{letra} é uma consoante!')
        break
    else:
        print('Error, é preciso digitar uma letra!')