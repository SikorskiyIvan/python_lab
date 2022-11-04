class Human:
    txt = input("введите что-нибудь..")
    def instancemethod(self):
        print("метод экзепляра класса Human")
        print(self.txt)
    @staticmethod
    def staticmethod(tmp):
        print(tmp)
    @classmethod
    def classmethod(cls):
        cls.txt = input("введите новую строку.....")
        print("метод класса, класса Human")
human = Human()

human.staticmethod("статический метод класса Human")
human.instancemethod()
human.classmethod(Human)

