import random


def create_arr(n, m):
    arr = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = random.randint(0, 20)
    return arr


def print_arr(arr):
    for row in arr:
        print(' | '.join([str(elem) for elem in row]))


n = int(input("Введите количество строк:"))
m = int(input("Введите количество столбцов:"))
arr = create_arr(n, m)
print_arr(arr)
temp = -1
for i in range(n):
    check = 0
    for j in range(m - 1):
        if arr[i][j] > arr[i][j + 1]:
            check = 1
    if check == 0:
        temp = i
        break
if not temp == -1:
    arr[temp].sort(reverse=True)
print_arr(arr)
