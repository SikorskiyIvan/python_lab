import math
import random

login = input("Введите логин:\n")
st = ('qwertyuiopasdfghjklzxcvbnmQWWERTYUIOPLKJHGFDSAMNBVCXZ')
n = 0;
passwr = ""
print("Вы хотите чтобы в пароле использовались цифры?\n1)Да\n2)Нет\n")
choice1 = int(input())

if (choice1 == 1):
    print("Вы хотите чтобы в пароле использовались символы?\n1)Да\n2)Нет\n")
    choice2 = int(input())
    if (choice2 == 1):
        st += "1234567890<>?';./,][()*&^%$#@!"
        while (n < 99):
            passwr += random.choice(st)
            n += 1
    else:
        st += "1234567890"
        while (n < 99):
            passwr += random.choice(st)
            n += 1
else:
    print("Вы хотите чтобы в пароле использовались символы?\n1)Да\n2)Нет\n")
    choice2 = int(input())
    if (choice2 == 1):
        st += "<>?';./,][()*&^%$#@!"
        while (n < 99):
            passwr += random.choice(st)
            n += 1
    else:
        while (n < 99):
            passwr += random.choice(st)
            n += 1

print("Ваш логин :", login)
print("Ваш рандомный пароль: ", passwr, "\n")
