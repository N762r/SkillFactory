import random
import time


maps = [' ', '1', '2', '3',
        '1', '-', '-', '-',
        '2', '-', '-', '-',
        '3', '-', '-', '-',
        ]


def check(x, y):
    if x == 1 and y == 1:
        if maps[5] == '-':
            return True
    elif x == 2 and y == 1:
        if maps[6] == '-':
            return True
    elif x == 3 and y == 1:
        if maps[7] == '-':
            return True
    elif x == 1 and y == 2:
        if maps[9] == '-':
            return True
    elif x == 2 and y == 2:
        if maps[10] == '-':
            return True
    elif x == 3 and y == 2:
        if maps[11] == '-':
            return True
    elif x == 1 and y == 3:
        if maps[13] == '-':
            return True
    elif x == 2 and y == 3:
        if maps[14] == '-':
            return True
    elif x == 3 and y == 3:
        if maps[15] == '-':
            return True


def step(x, y, symbol):
    if x == 1 and y == 1:
        maps[5] = symbol
    elif x == 2 and y == 1:
        maps[6] = symbol
    elif x == 3 and y == 1:
        maps[7] = symbol
    elif x == 1 and y == 2:
        maps[9] = symbol
    elif x == 2 and y == 2:
        maps[10] = symbol
    elif x == 3 and y == 2:
        maps[11] = symbol
    elif x == 1 and y == 3:
        maps[13] = symbol
    elif x == 2 and y == 3:
        maps[14] = symbol
    elif x == 3 and y == 3:
        maps[15] = symbol


def print_map():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2], end=" ")
    print(maps[3])

    print(maps[4], end=" ")
    print(maps[5], end=" ")
    print(maps[6], end=" ")
    print(maps[7])

    print(maps[8], end=" ")
    print(maps[9], end=" ")
    print(maps[10], end=" ")
    print(maps[11])

    print(maps[12], end=" ")
    print(maps[13], end=" ")
    print(maps[14], end=" ")
    print(maps[15])


def check_x():
    if maps[5] == 'x' and maps[6] == 'x' and maps[7] == 'x':
        print('Игрок "х" победил!')
    elif maps[9] == 'x' and maps[10] == 'x' and maps[11] == 'x':
        print('Игрок "х" победил!')
    elif maps[13] == 'x' and maps[14] == 'x' and maps[15] == 'x':
        print('Игрок "х" победил!')

    elif maps[5] == 'x' and maps[9] == 'x' and maps[13] == 'x':
        print('Игрок "х" победил!')
    elif maps[6] == 'x' and maps[10] == 'x' and maps[14] == 'x':
        print('Игрок "х" победил!')
    elif maps[7] == 'x' and maps[11] == 'x' and maps[15] == 'x':
        print('Игрок "х" победил!')

    elif maps[5] == 'x' and maps[10] == 'x' and maps[15] == 'x':
        print('Игрок "х" победил!')
    elif maps[13] == 'x' and maps[10] == 'x' and maps[7] == 'x':
        print('Игрок "х" победил!')
    else:
        return 0


def check_o():
    if maps[5] == 'o' and maps[6] == 'o' and maps[7] == 'o':
        print('Игрок "o" победил!')
    elif maps[9] == 'o' and maps[10] == 'o' and maps[11] == 'o':
        print('Игрок "o" победил!')
    elif maps[13] == 'o' and maps[14] == 'o' and maps[15] == 'o':
        print('Игрок "o" победил!')

    elif maps[5] == 'o' and maps[9] == 'o' and maps[13] == 'o':
        print('Игрок "o" победил!')
    elif maps[6] == 'o' and maps[10] == 'o' and maps[14] == 'o':
        print('Игрок "o" победил!')
    elif maps[7] == 'o' and maps[11] == 'o' and maps[15] == 'o':
        print('Игрок "o" победил!')

    elif maps[5] == 'o' and maps[10] == 'o' and maps[15] == 'o':
        print('Игрок "o" победил!')
    elif maps[13] == 'o' and maps[10] == 'o' and maps[7] == 'o':
        print('Игрок "o" победил!')
    else:
        return 0


def closestep_x():
    if maps[5] == 'x' and maps[6] == 'x' and maps[7] == '-':
        return 7
    elif maps[5] == 'x' and maps[6] == '-' and maps[7] == 'x':
        return 6
    elif maps[5] == '-' and maps[6] == 'x' and maps[7] == 'x':
        return 5

    elif maps[9] == 'x' and maps[10] == 'x' and maps[11] == '-':
        return 11
    elif maps[9] == 'x' and maps[10] == '-' and maps[11] == 'x':
        return 10
    elif maps[9] == '-' and maps[10] == 'x' and maps[11] == 'x':
        return 9

    elif maps[13] == 'x' and maps[14] == 'x' and maps[15] == '-':
        return 15
    elif maps[13] == 'x' and maps[14] == '-' and maps[15] == 'x':
        return 14
    elif maps[13] == '-' and maps[14] == 'x' and maps[15] == 'x':
        return 13

    elif maps[5] == 'x' and maps[9] == 'x' and maps[13] == '-':
        return 13
    elif maps[5] == 'x' and maps[9] == '-' and maps[13] == 'x':
        return 9
    elif maps[5] == '-' and maps[9] == 'x' and maps[13] == 'x':
        return 5

    elif maps[6] == 'x' and maps[10] == 'x' and maps[14] == '-':
        return 14
    elif maps[6] == 'x' and maps[10] == '-' and maps[14] == 'x':
        return 10
    elif maps[6] == '-' and maps[10] == 'x' and maps[14] == 'x':
        return 6
    
    elif maps[7] == 'x' and maps[11] == 'x' and maps[15] == '-':
        return 15
    elif maps[7] == 'x' and maps[11] == '-' and maps[15] == 'x':
        return 11
    elif maps[7] == '-' and maps[11] == 'x' and maps[15] == 'x':
        return 7

    elif maps[5] == 'x' and maps[10] == 'x' and maps[15] == '-':
        return 15
    elif maps[5] == 'x' and maps[10] == '-' and maps[15] == 'x':
        return 10
    elif maps[5] == '-' and maps[10] == 'x' and maps[15] == 'x':
        return 5

    elif maps[13] == 'x' and maps[10] == 'x' and maps[7] == '-':
        return 7
    elif maps[13] == 'x' and maps[10] == '-' and maps[7] == 'x':
        return 10
    elif maps[13] == '-' and maps[10] == 'x' and maps[7] == 'x':
        return 13
    else:
        return 0


def closestep_o():
    if maps[5] == 'o' and maps[6] == 'o' and maps[7] == '-':
        return 7
    elif maps[5] == 'o' and maps[6] == '-' and maps[7] == 'o':
        return 6
    elif maps[5] == '-' and maps[6] == 'o' and maps[7] == 'o':
        return 5

    elif maps[9] == 'o' and maps[10] == 'o' and maps[11] == '-':
        return 11
    elif maps[9] == 'o' and maps[10] == '-' and maps[11] == 'o':
        return 10
    elif maps[9] == '-' and maps[10] == 'o' and maps[11] == 'o':
        return 9

    elif maps[13] == 'o' and maps[14] == 'o' and maps[15] == '-':
        return 15
    elif maps[13] == 'o' and maps[14] == '-' and maps[15] == 'o':
        return 14
    elif maps[13] == '-' and maps[14] == 'o' and maps[15] == 'o':
        return 13

    elif maps[5] == 'o' and maps[9] == 'o' and maps[13] == '-':
        return 13
    elif maps[5] == 'o' and maps[9] == '-' and maps[13] == 'o':
        return 9
    elif maps[5] == '-' and maps[9] == 'o' and maps[13] == 'o':
        return 5

    elif maps[6] == 'o' and maps[10] == 'o' and maps[14] == '-':
        return 14
    elif maps[6] == 'o' and maps[10] == '-' and maps[14] == 'o':
        return 10
    elif maps[6] == '-' and maps[10] == 'o' and maps[14] == 'o':
        return 6
    
    elif maps[7] == 'o' and maps[11] == 'o' and maps[15] == '-':
        return 15
    elif maps[7] == 'o' and maps[11] == '-' and maps[15] == 'o':
        return 11
    elif maps[7] == '-' and maps[11] == 'o' and maps[15] == 'o':
        return 7

    elif maps[5] == 'o' and maps[10] == 'o' and maps[15] == '-':
        return 15
    elif maps[5] == 'o' and maps[10] == '-' and maps[15] == 'o':
        return 10
    elif maps[5] == '-' and maps[10] == 'o' and maps[15] == 'o':
        return 5

    elif maps[13] == 'o' and maps[10] == 'o' and maps[7] == '-':
        return 7
    elif maps[13] == 'o' and maps[10] == '-' and maps[7] == 'o':
        return 10
    elif maps[13] == '-' and maps[10] == 'o' and maps[7] == 'o':
        return 13
    else:
        return 0


game = True
count = 0
print('Вы хотите сыграть с другом или с компьютером?(0/1)')
_ = int(input())
if _ == 0:
    while game == True:
        print_map()
        while True:
            player_x = input('Игрок "x", ваш ход:')
            if check(int(player_x[0]), int(player_x[2])) == True:
                step(int(player_x[0]), int(player_x[2]), 'x')
                break
            else:
                print('Эта клетка занята, выберите другую!')
        if check_x() != 0:
            break
        count += 1
        if count == 9:
            print('Ничья!')
            break
        print_map()
        while True:
            player_o = input('Игрок "o", ваш ход:')
            if check(int(player_o[0]), int(player_o[2])) == True:
                step(int(player_o[0]), int(player_o[2]), 'o')
                break
            else:
                print('Эта клетка занята, выберите другую!')
        if check_o() != 0:
            break
        count += 1
        if count == 9:
            print('Ничья!')
            break
    print_map()
elif _ == 1:
    while game == True:
        print_map()
        while True:
            player_x = input('Игрок "x", ваш ход:')
            if check(int(player_x[0]), int(player_x[2])) == True:
                step(int(player_x[0]), int(player_x[2]), 'x')
                break
            else:
                print('Эта клетка занята, выберите другую!')
        if check_x() != 0:
            break
        count += 1
        if count == 9:
            print('Ничья!')
            break
        print_map()
        print('Ход компьютера')
        c_x = closestep_x()
        c_o = closestep_o()
        if c_o != 0:
            time.sleep(1)
            maps[c_o] = 'o'
        elif c_x != 0:
            time.sleep(1)
            maps[c_x] = 'o'
        else:
            while True:
                player_o = [random.randint(1, 4), ' ', random.randint(1,4)]
                time.sleep(1)
                if check(int(player_o[0]), int(player_o[2])) == True:
                    step(int(player_o[0]), int(player_o[2]), 'o')
                    break
        if check_o() != 0:
            break
        count += 1
        if count == 9:
            print('Ничья!')
            break
    print_map()
