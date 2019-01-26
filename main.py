import random
import os
import argparse

obj_arr = ['R', 'F', 'S', '*']
#R-Rock
#F-Fish
#S-Shrimp
#*-Empty

clear = lambda: os.system('cls')


def create_empty_ocean(ocean_len):
    temp_ocean = []
    # У океана есть "рамка" из пустых ячеек
    for i in range(ocean_len+2):
        temp_ocean.append([])
        for j in range(ocean_len+2):
            temp_ocean[i].append('*')
    return temp_ocean


def show_ocean(ocean, ocean_len):
    for i in range(1, ocean_len+1):
        for j in range(1, ocean_len+1):
            print(ocean[i][j], end=" ")
        print('\n')


if __name__ == '__main__':
    print('Введите длину стороны океана')
    ocean_len = int(input())

    ocean = create_empty_ocean(ocean_len)

    for i in range(1, ocean_len+1):
        for j in range(1, ocean_len+1):
            ocean[i][j] = random.choice(obj_arr)

    # Отображение первого океана
    show_ocean(ocean, ocean_len)

    esc = 0
    while esc == 0:
        print('Введите количество временных шагов:')
        time = int(input())
        time_count = 0

        while time_count < time:
            # Изначально все ячейки в океане пустые
            new_ocean = create_empty_ocean(ocean_len)
            for i in range(1, ocean_len+1):
                for j in range(1, ocean_len+1):
                    # Если в ячейке рыба
                    if ocean[i][j] == 'F':
                        fish_count = 0
                        for ti in range(i-1, i+2):
                            for tj in range(j-1, j+2):
                                if ocean[ti][tj] == 'F':
                                    fish_count += 1
                        if fish_count-1 == 3 or fish_count-1 == 2:
                            new_ocean[i][j] = 'F'
                    # Если в ячейке креветка
                    if ocean[i][j] == 'S':
                        shrimp_count = 0
                        for ti in range(i - 1, i + 2):
                            for tj in range(j - 1, j + 2):
                                if ocean[ti][tj] == 'S':
                                    shrimp_count += 1
                        if shrimp_count-1 == 3 or shrimp_count-1 == 2:
                            new_ocean[i][j] = 'S'
                    # Если ячейка пустая
                    if ocean[i][j] == '*':
                        fish_count = 0
                        shrimp_count = 0
                        for ti in range(i - 1, i + 2):
                            for tj in range(j - 1, j + 2):
                                if ocean[ti][tj] == 'F':
                                    fish_count += 1
                                if ocean[ti][tj] == 'S':
                                    shrimp_count += 1
                        if fish_count == 3:
                            new_ocean[i][j] = 'F'
                        elif shrimp_count == 3:
                            new_ocean[i][j] = 'S'
                    # Если в ячейке скала
                    if ocean[i][j] == 'R':
                        new_ocean[i][j] = 'R'
            # Отображение нового океана
            if new_ocean != ocean:
                print('Время: ', time_count)
                show_ocean(new_ocean, ocean_len)
                ocean = new_ocean
                time_count += 1
            else:
                print('Океан больше не изменяется')
                break
        print('Продолжить работу? (y/n)')
        answer = input()
        if answer == 'n' or answer == 'N':
            esc = 1
            clear()
        else:
            esc = 0




