import random

def rock_paper_scissors():
  while True:
    num = [1, 2, 3]
    computer = random.choice(num)
    print('Выбери предмет:')
    answer = int(input('1 - камень \n2 - ножницы \n3 - бумага\n'))
    if answer == computer:
      print('Ничья!')
    elif answer == 1:
      if computer == 2:
        print("Камень бьет ножницы! Вы победили!")
      else:
        print("Бумага оборачивает камень! Вы проиграли.")
    elif answer == 2:
      if computer == 3:
        print("Ножницы режут бумагу! Вы победили!")
      else:
        print("Камень бьет ножницы! Вы проиграли.")
    elif answer == 3:
      if computer == 1:
        print("Бумага оборачивает камень! Вы победили!")
      else:
        print("Ножницы режут бумагу! Вы проиграли.")
    elif answer == 4:
      break
    else:
      print('Ошибка ввода! Попробуйте еще раз.\n')
      rock_paper_scissors()

rock_paper_scissors()