"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

if __name__ == '__main__':
    pass

import random

INITIAL_NUMBER = 1
FINISH_NUMBER = 1000000

random_number = random.randint(INITIAL_NUMBER, FINISH_NUMBER)

message_with_range = f'от {INITIAL_NUMBER} до {FINISH_NUMBER}'

print(f'''Здравствуйте, пользователь!
Введите число в диапазоне {message_with_range}:''')

while True:
    entered_string = input()

    if 'exit' in entered_string.lower() or entered_string == '':
        break
    elif not entered_string.isnumeric():
        print('Вы ввели не число')
    else:
        entered_number = int(entered_string)

        if INITIAL_NUMBER <= entered_number <= FINISH_NUMBER:
            if entered_number < random_number:
                print('Введенное число меньше загаданного')
            elif entered_number > random_number:
                print('Введенное число больше загаданного')
            else:
                print('Вы угадали!')
                break
        else:
            print(f'Введенное число вне диапазона {message_with_range}')
