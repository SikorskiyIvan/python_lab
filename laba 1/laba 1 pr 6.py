lis = []
a = input("Введите числа через запятую:\n").split(",")
for i in range(0, len(a)):
    lis.append(a[i])
tup = tuple(lis)
print(lis,"\n",tup)
# print(lis.__sizeof__(),"\n", tup.__sizeof__())