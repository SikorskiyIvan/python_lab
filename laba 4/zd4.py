class Human:
    txt = input("Введите что-нибудь..ну пожалуйста...прошу..умоляю!")
    def instancemethod(self):
        print("Метод экземпляра класса Human")
        print(self.txt)
    @staticmethod
    def staticmethod(tmp):
        print(tmp)
    @classmethod
    def classmethod(cls):
        cls.txt = input("Введите новую строку.....")
        print("Метод класса, класса Human")
human = Human()

human.staticmethod("Статический метод класса Human")
human.instancemethod()
human.classmethod(Human)

