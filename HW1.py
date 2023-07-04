# ----1----
# a = input('Введите числа')
# b = a.split(' ')
# c = input('Введите строку')
# print(a, c)
# ----2----
# time_in_sec = int(input('Введите время в секундах'))
# hours = str(time_in_sec // 3600)
# minutes = str(((time_in_sec - 3600 * int(hours)) // 60))
# seconds = str(time_in_sec % 60)
# if len(hours) == 1:
#     hours = '0' + hours
# if len(minutes) == 1:
#     minutes = '0' + minutes
# if len(seconds) == 1:
#     seconds = '0' + seconds
# print(f'{hours}:{minutes}:{seconds}')
# ----3----
# n = input('Введите число n: ')
# n1 = int(n)
# n2 = int(n + n)
# n3 = int(n + n + n)
# print(n1 + n2 + n3)
# ----4----
# number = int(input('Введите число: '))
# max_num = 0
# while number > 0:
#     max_num = max(max_num, number % 10)
#     number = number // 10
# print(max_num)
# ----5----
# win = int(input('Введите прибыль фирмы: '))
# loss = int(input('Введите издержку фирмы: '))
# if win > loss:
#     print('Компания работает с прибылью')
#     print(f'Рентабельность выручки: {win/loss}')
#     employees = int(input('Введите количество сотрудников в фирме: '))
#     print(f'Прибыль фирмы а расчете на одного сотруднтика: {round(win/employees)}')
# elif win < loss:
#     print('Компания работает в убыток')
# ----6----
# a = int(input('Введите результат в первый день: '))
# b = int(input('Введите желаемый результат: '))
# day = 1
# while a < b:
#     piece = a / 10
#     a = a + piece
#     day += 1
# print(day)




