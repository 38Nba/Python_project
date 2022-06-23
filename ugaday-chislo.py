import random

spektr1 = int(input('От: '))
spektr2 = int(input('До: '))
count = 0
if spektr1 >= spektr2:
    print('Неверный ввод, первое число больше второго', end=' ')
    spektr1 = int(input('\nОт: '))

num_random = random.randint(spektr1, spektr2)

while True:
    num = int(input('\nУгадай число: '))
    if num != num_random:
        count += 1
        if num < num_random:
            print('Больше! Попробуй еще раз!', end='')
        elif num > num_random:
            print('Меньше! Попробуй еще раз!', end='')
    else:
        print('Поздравляю ты угадал!')
        print('Количество попыток:', count)
        break