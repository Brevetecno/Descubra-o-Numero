# Desenvolvedor Brevetecno
# Python 3
# 2019

# Descubra o número

import random

while True:
    print('-' * 50)
    print('{:^6}'.format('DESCUBRA O NÚMERO'))
    print('-' * 50)

    num = random.randint(1, 10)

    print(num)

    input()
