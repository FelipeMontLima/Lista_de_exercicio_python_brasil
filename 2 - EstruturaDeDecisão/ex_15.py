"""
15 -> Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

n1 = float(input('Digite o lado do triangulo: '))
n2 = float(input('Dígite o lado do triangulo: '))
n3 = float(input('Digite o lado fo triangulo: '))


if n1 != n2 != n3 and n1 != n3 != n2:
    print('Triangulo Escalento')
elif n1 == n2 == n3:
    print('Triangulo equilatero')
else:
    print('Triangulo Isóceles.')



