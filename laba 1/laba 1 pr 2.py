str = input("Введите строку:\n")
print("Самое длинное слово: ", max(str.split(), key = len))
print("Числа с четной длинной:\n")
for i in str.split():
    if(len(i) % 2 == 0):
        print (i)