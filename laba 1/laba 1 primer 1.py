print("Задание:\nВывести на экран все делители числа. Число вводить с клавиатуры.")
number = int(input("Ваше число:\n"))
i = 1
print("Делители рандомного числа:\n")
while(1):
    if (number % i == 0):
        print(i)
    if (i > number): break;
    i += 1