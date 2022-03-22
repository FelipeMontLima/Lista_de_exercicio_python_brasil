

n1 = float(input('Digite o lado do triangulo: '))
n2 = float(input('Dígite o lado do triangulo: '))
n3 = float(input('Digite o lado fo triangulo: '))


if n1 != n2 != n3 and n1 != n3 != n2:
    print('Triangulo Escalento')
elif n1 == n2 == n3:
    print('Triangulo equilatero')
else:
    print('Triangulo Isóceles.')



