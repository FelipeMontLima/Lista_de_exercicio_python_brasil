"""
11 -> Faça um programa que recebe o salário de um colaborador e o reajuste
segundo o seguinte critério, baseado no salário atual:

- salários até R$ 280,00 (incluindo) : aumento de 20%

- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%

- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%

salários de R$ 1500,00 em diante : aumento de 5% Após o
aumento ser realizado, informe na tela:

o salário antes do reajuste;

o percentual de aumento aplicado;

o valor do aumento;

o novo salário, após o aumento.
"""

while True:

    salario = input('Qual o Salário do colaborador: ')

    try:
        salario = float(salario)

        if 0 < salario <= 280:
            aumento = '20%'
            aumento_salario = salario * (20 / 100)
            novo_salario = salario + aumento_salario
            break

        elif 280 <= salario <= 700:
            aumento = '15%'
            aumento_salario = salario * (15 / 100)
            novo_salario = salario + aumento_salario
            break

        elif 700 <= salario <= 1500:
            aumento = '10%'
            aumento_salario = salario * (10 / 100)
            novo_salario = salario + aumento_salario
            break

        elif salario > 1500:
            aumento = '5%'
            aumento_salario = salario * (5 / 100)
            novo_salario = salario + aumento_salario
            break

        else:
            print('Error!!! VALOR INVÁLIDO!')

    except:
        print('ERROR, VALOR INVÁLIDO!')

print('=-' * 16)
print(f'Salário antes do ajuste: {salario}')
print(f'Aumento de {aumento}.')
print(f'Novo salário: {aumento_salario:.2f}')
print(f'Novo salário: {novo_salario:.2f}')
print('=-' * 16)


