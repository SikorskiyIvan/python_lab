
with open("F1.txt", 'w') as file1:
    data = input("Введите данные: ")
    while data:
        data = data + '\n'
        file1.write(data)
        data = input()
with open("F1.txt", 'r') as file1:
    with open("F2.txt", 'w') as file2:
        data = file1.readline()
        while data:
            check = True
            for i in data:
                if i.isdigit():
                    check = False
            if check:
                file2.write(data)
            data = file1.readline()