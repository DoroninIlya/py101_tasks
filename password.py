"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    pass

entered_password = input()

if (len(entered_password) >= 8 and entered_password.isalnum() and not
        entered_password.isalpha() and not entered_password.isnumeric()):
    print('сложный')
else:
    print('простой')
