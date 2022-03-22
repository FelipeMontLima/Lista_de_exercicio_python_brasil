"""
8 -> Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

while True:

    salario_hora = input('Quanto ganha o funcionario : ')
    hora_trabalho = input('Quantas horas trabalhada: ')

    try:
        salario_hora = float(salario_hora)
        hora_trabalho = int(hora_trabalho)

        if hora_trabalho <= 220:
            salario_bruto = salario_hora * hora_trabalho

            # Impostos
            ir = salario_bruto * (11 / 100)
            inss = salario_bruto * (8 / 100)
            sindicato = salario_bruto * (5 / 100)

            # Cálculos
            descontos = ir + inss + sindicato
            salario_liquido = salario_bruto - descontos

            # Resolução
            print()
            print('=-' * 15)
            print(f'Hora Trabalhada:.......{hora_trabalho}h')
            print(f'Salário Hora:........R${salario_hora}')
            print(f'Salário Bruto:.......R${salario_bruto}')
            print(f'IR (11%):............R${ir}')
            print(f'INSS (8%):...........R${inss}')
            print(f'Sindicato (5%):......R${sindicato}')
            print(f'Salário Liquído:.....R${salario_liquido}')
            print('=-' * 15)
            break
        else:
            print('A hora trabalhada precisa ser inferior à 220 horas ao mês!')
    except:
        print('É preciso digitar um valor para o calculo.')
