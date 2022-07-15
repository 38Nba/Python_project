def add_contact():
    new_contact = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if new_contact in contact_book:
        print('Такой человек уже есть в контактах.')
    else:
        new_number = input('Введите номер телефона: ')
        contact_book[new_contact] = new_number

        print('Текущий словарь контактов: {}'.format(contact_book))

def search():
    surname = input('Введите фамилию для поиска: ')
    if surname[-1] == 'а':
        surname = surname[:-1]
    for i_initials, i_age in contact_book.items():
        if surname == i_initials[0] or surname + 'а' == i_initials[0]:
            print(i_initials[0], i_initials[1], i_age)
        else:
            print('Такого человека нет в контактах.')
            break

def func():
    while True:
        action = input('Введите номер действия:\n 1. Добавить контакт\n 2. Найти человека\n')
        if action == '1':
            add_contact()
        if action == '2':
            search()

contact_book = dict()

func()
pass
