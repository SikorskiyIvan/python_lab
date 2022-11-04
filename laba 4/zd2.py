class Emploee:
    FIO = ""
    experience = ""
    salary = ""
    working_time = ""
    oklad = ""
    premium = ""
    def __init__(self):
        self.FIO = input("Введите ФИО..")
        self.experience = int(input("Введите стаж.."))
        self.salary = int(input("Введите почасовую зарплату.."))
        self.working_time = int(input("Введите количество отработанных часов.."))
        self.oklad = int(self.salary * self.working_time)
        if self.experience <= 1:
            self.premium = 0.01
        elif self.experience <= 3:
            self.premium = 0.05
        elif self.experience <= 5:
            self.premium = 0.08
        elif self.experience > 5:
            self.premium = 0.15

    def print_info(self):
        print("========================================================")
        print(f"ФИО: {self.FIO}")
        print(f"Стаж: {self.experience}")
        print(f"Почасовая зарплата: {self.salary}")
        print(f"Количество отработанных часов: {self.working_time}")
        print(f"Оклад: {self.oklad}")
        print(f"Премия: {self.premium * 100}% ({self.premium * self.oklad})")
        print("========================================================")
list_res = []
while True:
    print("1)Добавить сотрудника \n2)Вывести информацию о конкретном сотруднике \n3)Вывести информацию о всех сотрудниках\n0)Выход\nВаш выбор?..")
    choice = int(input())
    if choice == 1:
        a = Emploee()
        list_res.append(a)
    elif choice == 2:
        if not len(list_res) == 0:
            while True:
                numb = int(input("Введите номер сотрудника информацию о котором хотите получить.."))
                if numb < 0 or numb > len(list_res):
                    print("Введите корректное значение..")
                else:
                    break
            list_res[numb - 1].print_info()
        else:
            print("Список сотрудников пуст.")
    elif choice == 3:
        if not len(list_res) == 0:
            for i in range(len(list_res)):
                print(f"{i + 1} сотрудник")
                list_res[i].print_info()
                i = i + 1
        else: print("Список сотрудников пуст.")
    elif choice == 0:
        break
    else:
        print("Ввведите корректное значение...")
