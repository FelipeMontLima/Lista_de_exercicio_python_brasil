
n1 = int(input('Digite um bnúmero (1 - Domingo, 2 - segunda_feira...): '))

variavel = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabádo']

if 0 < n1 < 8:
    print(variavel[n1 - 1])

else:
    print('ERROR, é preciso digitar um valor entre 1 e 7!')