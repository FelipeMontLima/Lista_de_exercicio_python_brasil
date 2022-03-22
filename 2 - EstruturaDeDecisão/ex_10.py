"""
11 -> Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.
"""
while True:
    print('Qual horario você estuda?')
    horario = input('Dígite (M)Matutino, (V)Vespertino ou (N)Noturno: ').upper()

    if horario == 'M':
        print('Bom dia!')
        break
    elif horario == 'V':
        print('Boa Tarde!')
        break
    elif horario == 'N':
        print('Boa Noite!')
        break
    else:
        print('Valor Inválido!')