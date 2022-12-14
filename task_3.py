# Создайте программу для игры в ""Крестики-нолики"".

import random


def Start():
    while True:
        ans = input('начать игру?(y/n): ')
        if ans == 'n':
            return
        elif ans == 'y':
            return Game()
        else:
            continue


def Set_player():
    player = random.randint(0, 1)
    print(player)
    if player == 1:
        print('Вы ходите первым!')
    else:
        print('Первым ходит компьютер!')
    return player


def Game():
    line_1 = ['*', '*', '*']
    line_2 = ['*', '*', '*']
    line_3 = ['*', '*', '*']
    player = Set_player()
    while not Is_end(line_1, line_2, line_3):
        if player == 1:
            Human_move(line_1, line_2, line_3)
            print(str(line_1))
            print('\n' + str(line_2))
            print('\n' + str(line_3))
            player = 0
        else:
            Comp_move(line_1, line_2, line_3)
            print(str(line_1))
            print('\n' + str(line_2))
            print('\n' + str(line_3))
            player = 1



def Human_move(line_1, line_2, line_3):
    print('Ваш ход(x)')
    while True:
        str = int(input('Введите строку(1-3): '))
        col = int(input('Введите столбец(1-3): '))
        if str == 1: str = line_1
        if str == 2: str = line_2
        if str == 3: str = line_3
        if str[col - 1] == '*':
            str[col - 1] = 'x'
            return line_1, line_2, line_3
        else:
            print('Поле уже занято!')
            continue


def Comp_move(line_1, line_2, line_3):
    while True:
        print(f'ход компьютера(0)')
        str = random.randint(1,3)
        col = random.randint(1,3)
        if str == 1: str = line_1
        if str == 2: str = line_2
        if str == 3: str = line_3
        if str[col - 1] == '*':
            str[col - 1] = '0'
            return line_1, line_2, line_3
        else: continue


def Is_end(line_1, line_2, line_3):
    pl = '*'
    if (line_1[0] == line_2[0] == line_3[0]): pl = line_1[0]
    if (line_1[1] == line_2[1] == line_3[1]): pl = line_1[1]
    if (line_1[2] == line_2[2] == line_3[2]): pl = line_1[2]
    if (line_1[0] == line_1[1] == line_1[2]): pl = line_1[0]
    if (line_2[0] == line_2[1] == line_3[2]): pl = line_2[0]
    if (line_3[0] == line_3[1] == line_3[2]): pl = line_3[0]
    if (line_1[0] == line_2[1] == line_3[2]): pl = line_1[0]
    if (line_1[2] == line_2[1] == line_3[0]): pl = line_1[2]

    if pl == 'x':
        print('Вы выиграли!')
        return True
    if pl == '0':
        print(('Выиграл компьютер!'))
        return True
    if '*' not in line_1 or '*' not in line_2 or '*' not in line_3:
        print('Ничья')
        return True

Start()
