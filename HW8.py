# ----1----
# class Date:
#     date = ''
#
#     def __init__(self, date):
#         Date.date = date
#
#     @classmethod
#     def int_date(cls):
#         splitted_date = cls.date.split('-')
#         day = int(splitted_date[0])
#         month = int(splitted_date[1])
#         year = int(splitted_date[2])
#         return day, month, year
#
#     @staticmethod
#     def is_date_valid(day, month, year):
#         if 1 <= day <= 30 and  1 <= month <= 12 and 0 <= year <= 2023:
#             return True
# ----2----
# class ZeroDivErr(Exception):
#     def __init__(self, text):
#         self.text = text
#
# while True:
#     try:
#         s = 0
#         nums = input('Введите 2 сила через пробел: делимое и делитель: ').split()
#         if nums == 'stop':
#             break
#         if nums[1] == '0':
#             raise ZeroDivErr('Нельзя делить на ноль')
#         else:
#             print(int(nums[0]) / int(nums[1]))
#     except ZeroDivErr as err:
#         print(err)
# ----3----
# class NotNum(Exception):
#     def __init__(self, text):
#         self.text = text
#
# list_of_numbers = []
# while True:
#     try:
#         s = input('Введите число: ')
#         if s == '':
#             break
#         if s.isdigit() == False:
#             raise NotNum('Введите число! ')
#         else:
#             list_of_numbers.append(s)
#     except NotNum as NN:
#         print(NN)
#
#
# print(list_of_numbers)
# ----4,5,6----
# from abc import ABC
#
#
# class NotString(Exception):
#     def __init__(self, text):
#         self.text = text
#
#
# class StoreHouse(ABC):
#     num_of_tech = 0
#
#     @staticmethod
#     def send_to_store_house(cls, count=1):
#         try:
#             if type(count) == str:
#                 raise NotString('Количество обьектов должно быть цифрой, не строкой!')
#             if cls == 'Printer':
#                 Printer.printers -= count
#                 StoreHouse.num_of_tech -= count
#             if cls == 'Scaner':
#                 Scaner.scaners -= count
#                 StoreHouse.num_of_tech -= count
#             if cls == 'Xerox':
#                 Xerox.xeroxes -= count
#                 StoreHouse.num_of_tech -= count
#         except NotString as NS:
#             print(NS)
#
# @staticmethod def return_nums_of_tech(): return dict(printers=Printer.printers, scaners=Scaner.scaners,
# xeroxes=Xerox.xeroxes, total_tech=StoreHouse.num_of_tech)
#
#
# class Printer(StoreHouse, ABC):
#     printers = 0
#
#     def __init__(self):
#         super().__init__()
#         Printer.printers += 1
#         StoreHouse.num_of_tech += 1
#
#
# class Scaner(StoreHouse, ABC):
#     scaners = 0
#
#     def __init__(self):
#         super().__init__()
#         Scaner.scaners += 1
#         StoreHouse.num_of_tech += 1
#
#
# class Xerox(StoreHouse, ABC):
#     xeroxes = 0
#
#     def __init__(self):
#         super().__init__()
#         Xerox.xeroxes += 1
#         StoreHouse.num_of_tech += 1
#
#
# printer1 = Printer()
# printer2 = Printer()
# scaner1 = Scaner()
# storehouse = StoreHouse()
# StoreHouse.send_to_store_house('Printer', 1)
# print(StoreHouse.return_nums_of_tech())
# ----7----
# class Complex:
#     def __init__(self, num1):
#         self.num1 = num1
#
#     def __str__(self):
#         return str(self.num1)
#
#     def __add__(self, other):
#         return Complex(self.num1 + other.num1)
#
#     def __mul__(self, other):
#         return Complex(self.num1 * other.num1)
#
#
# num1 = Complex(1 + 2j)
# num2 = Complex(2 + 3j)
# print(num1 * num2)
