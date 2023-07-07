# ----1----
# from time import sleep
#
#
# class TrafficLight:
#     _color = 'red'
#
#     def __init__(self, cycles):
#         self.cycles = cycles
#
#     def running(self):
#         cnt = 0
#         while True:
#             if cnt == self.cycles:
#                 break
#             self._color = 'red'
#             print(self._color)
#             sleep(7)
#             self._color = 'yellow'
#             print(self._color)
#             sleep(2)
#             self._color = 'green'
#             print(self._color)
#             sleep(7)
#             cnt += 1
#
#
# TL = TrafficLight(int(input('Введите количество циклов: ')))
# TL.running()
# ----2----
# class Road:
#     def __init__(self, length, width, weight_per_cm, cm):
#         self.__length = length
#         self.__width = width
#         self.weight = weight_per_cm
#         self.cm = cm
#
#     def asphalt_weight(self):
#         weight = self.__length * self.__width * self.weight * self.cm
#         if weight > 10000:
#             if weight % 10 == 0:
#                 print(int(weight / 1000), 'т', sep = '')
#             else:
#                 print(weight / 1000, 'т', sep='')
#         else:
#             print(weight)
#
#
# a = Road(20, 2500, 25, 5)
# a.asphalt_weight()
# ----3----
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self.wage = int(wage)
#         self.bonus = int(bonus)
#         self.__income = {'wage': wage, 'bonus': bonus}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         print('Имя и фамилия: ' + self.name + ' ' + self.surname)
#
#     def get_total_income(self):
#         print('Итоговая зарплата: ' + str(self.wage + self.bonus))
#
#
# a_z = Position('Amir', 'Ziatdinov', 'Boss', 10000, 100)
# a_z.get_full_name()
# a_z.get_total_income()
# ----4----
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed, self.color, self.name, self.is_police = speed, color, name, is_police
#
#     def show_speed(self):
#         print('Текущая скорость -', self.speed)
#
#     def stop(self):
#         print('Машина остановилась')
#         self.speed = 0
#
#     def go(self):
#         print('Машина поехала')
#         if self.speed == 0:
#             self.speed = 40
#
#     def turn_right(self):
#         print('Машина повернула направо')
#         self.speed = 20
#
#     def turn_left(self):
#         print('Машина повернула налево')
#         self.speed = 20
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             print('Превышение скорости!')
#         else:
#             print('Текущая скорость -', self.speed)
#
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             print('Превышение скорости!')
#         else:
#             print('Текущая скорость -', self.speed)
#
#
# class PoliceCar(Car):
#     @staticmethod
#     def migalka():
#         print('ВИУ ВИУ ВИУ ВИУ ВИУ ВИУ ВИУ ВИУ ВИУ')
# ----5----
# class Stationary:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
#
# class Pen(Stationary):
#     def draw(self):
#         print('Рисую ручкой')
#
#
# class Pencil(Stationary):
#     def draw(self):
#         print('Рисую карандашом')
#
#
# class Handle(Stationary):
#     def draw(self):
#         print('Рисую маркером')