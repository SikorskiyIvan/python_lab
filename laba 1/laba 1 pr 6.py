lis = []
a = input("Введите числа через запятую:\n").split(",")
for i in range(0, len(a)):
    lis.append(a[i])
tup = tuple(lis)
print(lis," ",tup)
print(lis.__sizeof__()," ", tup.__sizeof__())