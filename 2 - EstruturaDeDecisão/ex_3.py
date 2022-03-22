"""
3 -> Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra
escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

while True:

    genero = input('Digite "F" para Feminino, "M" para Masculino e "T" para Pessoa Trans: ').upper()

    if genero == 'F':
        print(f'{genero} - Feminino')
        break

    elif genero == 'M':
        print(f'{genero} - Masculino.')
        break

    elif genero == 'T':
        print(f'{genero} - Trans.')
        break
    else:
        print('É preciso digitar um gênero catalogado!')
