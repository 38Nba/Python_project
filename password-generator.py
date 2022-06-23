import random

generator_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$%&\?@'
long_password = int(input('Введите длину пароля: '))

while True:
    quantity = int(input('Введите количество паролей: '))
    for i_quantity in range(quantity):
        if i_quantity != quantity:
            print(''.join(random.sample(generator_list, long_password)))
    else:
        break