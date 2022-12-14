# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def Start():
    while True:
        ans = input('начать игру?(y/n): ')
        if ans == 'n':
            return
        elif ans == 'y':
            return Set_player()
        else:
            continue


def Set_player():
    player = random.randint(0, 1)
    print(player)
    if player == 1:
        print('Вы ходите первым!')
    else:
        print('Первым ходит компьютер!')
    Game(player)


def Game(player):
    value = 300
    while value:
        if player == 1:
            move = Human_move(value)
            player = 0
        else:
            move = Comp_move(value)
            player = 1
            print(f'ход компьютера - {move}')
        value -= move
        print(f'Осталось конфет - {value}')
        if value == 0 and player == 0:
            print('Вы выиграли!')
            return
        if value == 0 and player == 1:
            print('Увы, Вы проиграли(')
            return


def Human_move(value):
    while True:
        if value < 28: lim = value
        else: lim = 28
        move = int(input('Введите количество конфет(от 1 до 28)'))
        if move < 1 or move > lim: continue
        else: return move

def Comp_move(value):
    if value <= 28:
        move = value
    elif value % 29 != 0:
        move = value % 29
    else: move = 28

    return move
    #     lim = value
    # else: lim = 28
    # return random.randint(1, lim)

Start()
