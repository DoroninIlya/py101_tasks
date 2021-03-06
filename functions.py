"""Задания по ветвлениям, итерациям и вводу данных."""

import keyword

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное


def check_parity_numbers(numbers):
    formated_numbers = numbers.replace(' ', '').split(',')
    is_even_number = False

    for number in formated_numbers:
        if not number.isdigit():
            continue
        elif int(number) % 2 == 0:
            is_even_number = True
            break

    return is_even_number

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
SELLING_IS_ALLOWED = 'Продажа разрешена'
SELLING_IS_DISALLOWED = 'Мы не продаём алкоголь несовершеннолетним.'


def sell_alcohol(number_of_years):
    allowed_age = 21

    return number_of_years >= allowed_age

print(SELLING_IS_ALLOWED if sell_alcohol(age) else SELLING_IS_DISALLOWED)

# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()


def is_keyword(word):
    return keyword.iskeyword(word)

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."


def get_type(data):
    types = {
        'int': 'Это число',
        'str': 'Это строка',
        'bool': 'Это булевый',
        'NoneType': 'Это None',
        'tuple': 'Это кортеж',
        'list': 'Это список',
        'set': 'Это множество',
        'dict': 'Это словарь',
        }

    data_type = 'Неизвестный тип данных'

    for type_from_dictionary in types.keys():
        if type_from_dictionary in str(type(data)):
            data_type = types[type_from_dictionary]
            break
    return data_type
