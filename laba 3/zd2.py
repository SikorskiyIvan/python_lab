with open('data_zd2.txt', 'r', encoding="utf-8") as read_file:
    data = read_file.readline()
    print("Зарплата больше 2000: ")
    while data:
        if int(data.split()[1]) > 2000:
            print(data.split()[0])
        data = read_file.readline()
    read_file.seek(0)
    data = read_file.readline()
    min_zp = int(data.split()[1])
    while data:
        if int(data.split()[1]) < min_zp:
            min_zp = int(data.split()[1])
            min_name = data
        data = read_file.readline()
    print("Минимальная зарпалата: ", min_name)
