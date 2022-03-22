"""
2 -> Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""
while True:
    n1 = input('Digite um valor: ')

    if n1.isdigit():

        n1 = int(n1)

        print(f'O número digitado foi {n1}.')
        break
    else:
        print(f'{n1} não é um número, é preciso digitar um NÚMERO.')