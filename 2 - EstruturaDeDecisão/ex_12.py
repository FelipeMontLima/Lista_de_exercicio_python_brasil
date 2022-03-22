"""
12 -> Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento

Salário Bruto até 1500 (inclusive) - desconto de 5%

Salário Bruto até 2500 (inclusive) - desconto de 10%

Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""


salario_hora = input('Quanto é o salário por hora: ')
hora_trabalhada = input('Quanto trabalhado no mês: ')

try:
    salario_hora = float(salario_hora)
    hora_trabalhada = int(hora_trabalhada)

    salario_bruto = salario_hora * hora_trabalhada

    #impostos
    inss = salario_bruto * (10/100)
    fgts = salario_bruto * (11/100)


    if 0 < salario_bruto <= 900:
        ir = 'ISENTO'
        salario_liquido = salario_bruto - inss

    elif 900 < salario_bruto <= 1500:
        ir = salario_bruto * (5/100)
        salario_liquido = salario_bruto - ir - inss

    elif 1500 <= salario_bruto <= 2500:
        ir = salario_bruto * (10/100)
        salario_liquido = salario_bruto - ir - inss

    elif salario_bruto > 2500:
        ir = salario_bruto * (20/100)
        salario_liquido = salario_bruto - ir - inss

    else:
        print('ERROR, isso não é um valor salarial.')

    print(f'Salário Bruto: {salario_bruto}')
    print(f'IR: {ir}')
    print(f'INSS: {inss}')
    print(f'FGTS: {fgts}')
    print(f'Salário Liquído: {salario_liquido}')


except:
    print('Error, é preciso valores para calculo do salário!')

