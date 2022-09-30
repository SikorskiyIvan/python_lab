import json

with open("data_zd4.txt", 'r', encoding="utf-8") as file:
    str = file.readline()
    n = 1
    m = 1
    summ = 0
    while str:
        tmp = int(str.split()[2]) - int(str.split()[3])
        print(f"Прибыль {n} компании - {tmp}")
        str = file.readline()
        n += 1
        if tmp > 0:
            summ += tmp
            m += 1
    average = summ / m
    print("Средняя прибыль:", average)
    diction = {}
    list1 = [diction, {"average_profit": average}]
    file.seek(0)
    str = file.readline()
    while str:
        diction[str.split()[0]] = int(str.split()[2]) - int(str.split()[3])
        str = file.readline()
    print(list1)
    with open("data_zd4.json", "w") as file1:
        json.dump(list1, file1)