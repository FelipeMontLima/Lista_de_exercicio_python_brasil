"""
15 ->Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido:
"""

while True:
    salario_bruto = input('Digite o salário do funcionário: ')

    try:
        salario_bruto = float(salario_bruto)
        ir = salario_bruto * (11 / 100)
        inss = salario_bruto * (8 / 100)
        sindicato = salario_bruto * (5 / 100)
        descontos = ir + inss + sindicato
        salario_liquido = salario_bruto - descontos


        break

    except:
        print('É preciso digitar um valor para o cálculo!')

print('=-' * 15)
print(f'+Salário Bruto: R$ {salario_bruto:.2f}')
print(f'-IR (11%): R$ {ir:.2f}')
print(f'-INSS (8%): R$ {inss:.2f}')
print(f'-Sindicato (5%): R$ {sindicato:.2f}')
print(f'+Salário Líquido: R$ {salario_liquido:.2f}')
print('=-' * 15)