# Desenvolvedor Brevetecno
# Python 3
# 2019

# Descubra o número

import random

loop1 = True
loop2 = True

while loop1:
    loop2 = True
    print('-' * 50)
    print('{:^6}'.format('DESCUBRA O NÚMERO'))
    print('-' * 50)

    n1 = int(input('Menor número: '))
    n2 = int(input('Maior número: '))
    print('O número será gerado entre {} a {}.'.format(n1, n2))

    input('Aperte ENTER para gerar um número aleatório')

    print('-' * 50)
    num = random.randint(n1, n2)
    print('O número gerado foi: ', num)


    while loop2:
        print('-' * 50)
        print('(1) - Continuar')
        print('(2) - Sair')
        resposta = int(input('Resposta: '))

        if (resposta == 1):
            loop1 = True
            loop2 = False
        elif (resposta == 2):
            exit()
        else:
            print('-' * 50)
            print('Digite 1 ou 2')
            loop2 = True

