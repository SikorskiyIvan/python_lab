class Zoo:
    def movement(self):
        print("movement для Zoo")
class Animal(Zoo):
    def movement(self):
        print("movement для Animal")
class Fish(Animal):
    classif = "Окунь"
    price = 100
    def movement(self):
        print("movement для Fish")
class Bird(Animal):
    classif = "Галка"
    price = 200
    def movement(self):
        print("movement для Bird")
with open("data.txt", "w", encoding="utf-8") as file:
    list = []

    zoo = Zoo()
    animal = Animal()
    fish = Fish()
    bird = Bird()

    zoo.movement()
    animal.movement()
    fish.movement()
    bird.movement()

    print("")
    if fish.price > bird.price:
        biggest_price = fish.classif
    else:
        biggest_price = bird.classif
    words = "Самая дорогая порода: " + biggest_price
    print(words)
    list.append(words)
    file.write(words)