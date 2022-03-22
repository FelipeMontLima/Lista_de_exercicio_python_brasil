"""
5 -> Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""


while True:
    print('Dígita as notas do aluno!')
    n1 = input('Nota 1: ')
    n2 = input('Nota 2: ')
    n3 = input('Nota 3: ')
    n4 = input('Nota 4: ')

    try:
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
        n4 = float(n4)

        media = (n1 + n2 + n3 + n4) / 4

        if media == 10:
            print(f'{media} Aprovado com Distição!')
        elif media >= 7:
            print(f'{media:.2f} Aprovado!')
        else:
            print(f'{media:.2f} Reprovado!')
        break

    except:
        print('É preciso dígitar valores para a média!')
