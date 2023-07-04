# ----1----
# a = [1, 'wdfwef', True, False, [312413, 1234]]
# for i in a:
#     print(type(i))
# ----2----
# elements = []
# while True:
#     a = input('Введите элемент. Для выхода нажмите enter')
#     if a == '':
#         break
#     elements.append(a)
# for i in range(0, len(elements)-1, 2):
#     a1 = elements[i]
#     a2 = elements[i + 1]
#     elements[i] = a2
#     elements[i + 1] = a1
# print(elements)
# ----3.1----
# months = ['Зима', 'Весна', 'Лето', 'Осень']
# month_num = int(input('Введите номер месяца: '))
# if 1 <= month_num <= 2 or month_num == 12:
#     print(months[0])
# elif 3 <= month_num <= 5:
#     print(months[1])
# elif 6 <= month_num <= 8:
#     print(months[2])
# elif 9 <= month_num <= 11:
#     print(months[3])
# ----3.2----
# months = dict(Winter=[12, 1, 2], Spring=[3, 4, 5], Summer=[6, 7, 8], Autumn=[9, 10, 11])
# month_num = int(input('Введите номер месяца: '))
# for i in months:
#     if month_num in months.get(i):
#         print(i)
# ----4----
# a = input('Введите слова: ').split()
# cnt = 1
# for i in a:
#     if len(i) > 10:
#         i = i[:10]
# for i in a:
#     print(f'{cnt}: {i}')
#     cnt += 1
# for cnt, i in enumerate(a, start=1):
#     print(f'{cnt}: {i}')
# ----5----
# my_list = [7, 5, 3, 3, 2]
# while True:
#     a = input('Введите цифру. Для выхода нажмите return: ')
#     if a == '':
#         print('Ввод завершен')
#         break
#     my_list.append(int(a))
#     my_list.sort(reverse=True)
#     print(my_list)
# ----6----
# list_of_products = []
# cnt = 1
# while True:
#     name = input('Введите название товара: ')
#     price = input('Введите цену товара: ')
#     number = input('Введите количество товара: ')
#     my_tuple = (cnt, dict(название=name, цена=price, количество=number, ед='шт.'))
#     list_of_products.append(my_tuple)
#     cont = input('Нажмите return чтобы выйти. Для продолжения нажмите любую клавишу ')
#     if cont == '':
#         break
#     else:
#         continue
# names = []
# prices = []
# numbers = []
# pieces = []
# for i in list_of_products:
#     for j in i:
#         if type(j) == int:
#             continue
#         names.append(j.get('название'))
#         prices.append(j.get('цена'))
#         numbers.append(j.get('количество'))
#         pieces.append(j.get('ед'))
# pieces = list(set(pieces))
# names = list(set(names))
# numbers = list(set(numbers))
# prices = list(set(prices))
# final_dict = dict(названия=names, цены=prices, количества=numbers, ед=pieces)
# for key, value in final_dict.items():
#     print(f'{key}: {value}')














