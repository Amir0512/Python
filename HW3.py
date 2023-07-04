# ----1----
# def Devide(a, b):
#     print(a / b)
#
#
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# try:
#     Devide(a, b)
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# ----2---
# def User(name=input('Введите имя: '), surname=input('Введите фамилию: '), birth_date=input('Введите год рождения: ')
#          ,city=input('Введите город проживания: '), email=input('Введите email: '), phone=input('Введите номер телефона: ')):
#         print(f'имя - {name}, фамилия - {surname}, год рождения - {birth_date}, город - {city}, почта - {email}, '
#               f'номер телефона - {phone}')
#
#
# User()
# ----3----
# def my_func(a, b, c):
#     max_1 = max(a, b, c)
#     max_2 = a + b + c - max_1 - min(a, b, c)
#     return max_1, max_2
#
#
# print(my_func(10, 23, 21))
# ----4----
# def my_func(x, y):
#     a = x * x
#     for i in range(y):
#         a = a * x
#     return int(a / x / x)
#
#
# print(my_func(3, 7))
# ----5----
# b = 0
# while True:
#     a = input('Введите числа через пробел. Для выхода нажмите k: ').split()
#     if len(a) == 1 and 'k' in a:
#         print(b)
#         break
#     elif len(a) > 1 and a[-1] == 'k':
#         a.remove('k')
#         c = map(int, a)
#         b += sum(c)
#         print(b)
#         break
#     else:
#         c = map(int, a)
#         b += sum(c)
#         print(b)
# ----6----
# def int_func(word):
#     return word.title()
#
#
# title_words = []
# words = input('Введите слова строчной буквы через пробел: ').split()
# for i in words:
#     title_word = int_func(i)
#     title_words.append(title_word)
# print(' '.join(title_words))
