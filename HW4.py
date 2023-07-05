# ----1----
# from sys import argv
# name, hours, salary, prem = argv
# print(int(hours) * int(salary) + int(prem))
# ----2----
# from random import randint
# from sys import argv
# name, start, end, rang = argv
# my_list = [randint(int(start), int(end)) for i in range(int(rang))]
# my_list.sort()
# final_list = []
# first_half = my_list[int(rang)//2:]
# second_half = my_list[:int(rang)//2]
# if int(rang) % 2 == 0:
#     for i in range(len(first_half)):
#         final_list.append(second_half[i])
#         final_list.append(first_half[i])
# else:
#     for i in range(len(first_half)-1):
#         final_list.append(second_half[i])
#         final_list.append(first_half[i])
#     final_list.append(first_half[-1])
# print(final_list)
# ----3----
# a = [print(i) for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
# ----4----
# from random import randint
# my_list = [randint(1, 10) for i in range(8)]
# str_list = list(map(str, my_list))
# final_list = []
# for i in str_list:
#     if str_list.count(i) == 1:
#         final_list.append(i)
# print(my_list, final_list)
# ----5----
# from functools import reduce
# def plus(a, b):
#     return a * b
#
#
# my_list = [i for i in range(100, 1001) if i % 2 == 0]
# print(reduce(plus, my_list))
# ----6.1----
# from itertools import count
# for i in count(10):
#     if i == 100:
#         break
#     print(i)
# ----6.2----
# from itertools import cycle
# my_list = ['A', 'B', "D", 2, 5]
# cnt = 0
# for i in cycle(my_list):
#     if cnt == 100:
#         break
#     print(i)
#     cnt += 1
# ----7----
# from math import factorial
# def fact(n):
#     for el in range(1, n + 1):
#         yield factorial(el)
#
#
# for el in fact(10):
#     print(el)