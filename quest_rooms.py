def bedroom():
  door = int(input('Вы в спалне. Куда идём? \n1 - вваную \n2 - в коридор \n'))

  if door == 1:
    bathroom()
  elif door == 2:
    coridors()
  else:
    print('Ошибка ввода! Попробуйте еще раз.')
    door = int(input('Вы в спалне. Куда идём? \n1 - вваную \n2 - в коридор \n'))

def kitchen():
  door = int(input('Вы на кухне. Куда идём? \n1 - коридор \n2 - окно \n'))
  if door == 2:
    print("Вы проиграли ")
  elif door == 1:
      coridors()

  play = int(input('Сыграем ещё раз? \n1 - да \n2 - нет \n'))

  while True:
    if play == 1:
      quest()
    elif play == 2:
      print('Игра окончена!')
      break
    else:
      print('Ошибка ввода! Попробуйте еще раз.')
      play = int(input('Сыграем ещё раз? \n1 - да \n2 - нет \n'))


def coridors():
  door = int(input('Вы в коридоре. Куда идём? \n1 — в спальню \n2 — в ванную \n3 — на кухню \n4 — дверь внаружу \n'))

  if door == 1:
    bedroom()
  elif door == 2:
    bathroom()
  elif door == 3:
    kitchen()
  elif door == 4:
    print('Вы выиграли!')
    play = int(input('Сыграем ещё раз? \n1 - да \n2 - нет \n'))

  while True:
    if play == 1:
      quest()
    elif play == 2:
      print('Игра окончена!')
      break
    else:
      print('Ошибка ввода! Попробуйте еще раз.')
      play = int(input('Сыграем ещё раз? \n1 - да \n2 - нет \n'))

def bathroom():
  door = int(input('Вы в ванной. Куда идём? \n1 — в коридор \n2 — в спальню \n'))

  if door == 1:
    coridors()
  elif door == 2:
    bedroom()
  else:
    print('Ошибка ввода! Попробуйте еще раз.')
    door = int(input('Вы в ванной. Куда идём? \n1 — в коридор \n2 — в спальню \n'))


def quest():

  door = int(input('Добро пожаловать в игру!. Перед вами 3 двери. Куда идем? \n1 - спальня \n2 - кухня \n3 - ванная \n'))
  if door == 1:
    bedroom()
  elif door == 2:
    kitchen()
  else:
    bathroom()
quest()