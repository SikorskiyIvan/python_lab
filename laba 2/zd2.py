def z1(data):
    if type(data) == list:
        n = len(data)
        check = 0
        sum_1 = 0
        second_null, first_null = -1, -1
        for i in range(n):
            if check == 1:
                if data[i] == 0:
                    second_null = i
                    break
            if data[i] == 0:
                first_null = i
                check = 1
        if not second_null == -1:
            if not first_null == -1:
                for i in range(first_null, second_null):
                    sum_1 += data[i]
        else :
            print("\nНет двух нулей")
            return
        print(f"\nсписок-{sum_1}")
    elif type(data) == int:
        st = str(data)
        sum = 0
        for i in st:
            if int(i) % 2 == 0:
                sum += int(i)
        print(f"число-{sum}")
    elif type(data) == tuple:
        data = list(data)
        n = 0
        max_ = max(data)
        min_ = min(data)
        n = len(data)
        for i in range(n):
            if (max_ == data[i]):
                max_i = i
            if (min_ == data[i]):
                min_i = i
        data[max_i] = min_
        data[min_i] = max_
        new_data = tuple(data)
        print(f"кортеж-{new_data}")
    elif type(data) == str:
        print("строка-", end='')
        for i in data:
            print(f"{ord(i)}",end=' ')
z1(1234)
z1("blihfutd")
z1([12,0,32,54,324,0,5])
z1((32,423,5312,43,5,32))