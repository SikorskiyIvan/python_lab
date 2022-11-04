class Human:
    def instancemethod(self):
        print("метод экзепляра класса Human")
    @staticmethod
    def staticmethod(tmp):
        print(tmp)
    @classmethod
    def classmethod(cls):
        print("метод класса, класса Human")
human = Human()
human.staticmethod("статический метод класса Human")
human.instancemethod()
human.classmethod()

