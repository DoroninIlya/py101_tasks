"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""

if __name__ == '__main__':
    pass

INITIAL_NUMBER = 1
FINISH_NUMBER = 101

NUMBER_FOR_ZIP = 3
NUMBER_FOR_ZAP = 5
NUMBER_FOR_ZIPZAP = 15

for number in range(INITIAL_NUMBER, FINISH_NUMBER):
    if number % NUMBER_FOR_ZIP == 0 and number % NUMBER_FOR_ZIPZAP != 0:
        print('zip')
    elif number % NUMBER_FOR_ZAP == 0 and number % NUMBER_FOR_ZIPZAP != 0:
        print('zap')
    elif number % NUMBER_FOR_ZIPZAP == 0:
        print('zip-zap')
    else:
        print(number)