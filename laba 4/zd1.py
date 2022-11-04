
class Example:
    static1, static2 = 10, 20
    dynamic1 = int(input("Введите 1 динамическую переменную..."))
    dynamic2 = int(input("Введите 2 динамическую переменную..."))
    def first(self):
        exam = input("Введите переменную...")
        print(f"Ваша переменная - {exam}")
    def second(self):
        print(f"Сумма двух переменных - {Example.static1 + Example.static2}")
    def third(self):
        print(f"{Example.dynamic1} в {Example.dynamic2} степени - {pow(Example.dynamic1, Example.dynamic2)}")
a = Example()
a.first()
a.second()
a.third()
print(a)
