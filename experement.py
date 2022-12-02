# class Emploee:
#     FIO = ""
#     experience = ""
#     salary = ""
#     working_time = ""
#     oklad = ""
#     premium = ""
#     def __init__(self):
#         self.FIO = input("Введите ФИО..")
#         self.experience = int(input("Введите стаж.."))
#         self.salary = int(input("Введите почасовую зарплату.."))
#         self.working_time = int(input("Введите количество отработанных часов.."))
#         self.oklad = int(self.salary * self.working_time)
#         if self.experience <= 1:
#             self.premium = 0.01
#         elif self.experience <= 3:
#             self.premium = 0.05
#         elif self.experience <= 5:
#             self.premium = 0.08
#         elif self.experience > 5:
#             self.premium = 0.15
#
#     def print_info(self):
#         print("========================================================")
#         print(f"ФИО: {self.FIO}")
#         print(f"Стаж: {self.experience}")
#         print(f"Почасовая зарплата: {self.salary}")
#         print(f"Количество отработанных часов: {self.working_time}")
#         print(f"Оклад: {self.oklad}")
#         print(f"Премия: {self.premium * 100}% ({self.premium * self.oklad})")
#         print("========================================================")
# list_res = []
# a = Emploee()
# list_res.append(a)
# a = Emploee()
# list_res.append(a)
# if not len(list_res) == 0:
#     for i in range(len(list_res)):
#         print(f"{i + 1} сотрудник")
#         list_res[i].print_info()
#         i = i + 1
# else: print("Список сотрудников пуст.")

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot()

y = np.random.normal(0, 2, 500)
ax.hist(y)
ax.grid()

plt.show()
