

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Dgite a segunda nota: '))
media = (n1 + n2) / 2

if 10 >= media >= 9:
    print(f'APROVADO: A {media}')
elif 9 > media >= 7.5:
    print(f'Aprovado: B {media}')
elif 7.5 > media >= 6:
    print(f'APROVADO: C {media}')
elif 6 > media >= 4:
    print(f'REPROVADO: D {media}')
elif 4 > media >= 0:
    print(f'REPROVADO: E {media}')
else:
    print('ERROR, É PRECISO UM VALOR PARA A MEDIA')