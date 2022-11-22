import random as r
from math import log2, ceil

def is_valid(n): # проверка значения
    return n.isdigit() and float(n) - int(float(n)) == 0 and 1 <= int(n) <= 100

def guess(a, b): # логика игры
    num = r.randint(a, b)
    count = ceil(log2(b))
    total = 0
    for i in range(count + 1):
        n = input_num()
        total += 1
        if total == count:
            print('У вас кончились попытки. Попробуйте снова')
            break
        elif n > num:
            print(f'У вас осталось {count - i} попыток')
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n < num:
            print(f'У вас осталось {count - i} попыток')
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print(f'Поздравляю! Вы угадали! Колличество попыток: {total}')
            break

def input_num(): # ввод данных
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('Может введем число в диапозоне от 1 до 100?')

def game(): # игра
    print('Добро пожаловать в числовую угадайку!')
    while True:
        print('Введи числа через Enter, в каком диапозоне чисел будем играть?:')
        a, b = input_num(), input_num()
        if b < a:
            a, b = b, a
        print(f'Введите число от {a} до {b}:')
        guess(a, b)
        if continue_game():
            continue
        else:
            break

def continue_game(): # продолжение игры
    print('Хотите сыграть еще раз?("д"/"н")')
    answer = input().lower()
    while True:
        if answer not in ('y','n','д','н'):
            print('Не понял? Да или нет?')
            answer = input().lower()
        elif answer in ('y','д'):
            print('Продолжим!')
            return True
        else:
            return False

game() # вызов игры
print('Спасибо что играли в числовую угадайку')