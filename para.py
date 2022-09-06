import random

str = input("Введите строку: ")
sym = input("Введите символ: ")
new_str = ""
c = len(str)
a = 0
while(a <= c):
    if str[a] == sym[0]:
        a+=1
    else:
        new_str += str[a]
        a+=1
print(new_str)