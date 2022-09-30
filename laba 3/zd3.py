with open("data_zd3.txt", 'r', encoding="utf-8") as file:
    data = file.readline()
    diction = {}
    while data:
        hours = 0
        check = 0
        for word in data.split():
            if check == 1:
                numb = word[0] + word[1]
                hours += int(numb)
            check = 1
        diction[data.split()[0]] = hours
        data = file.readline()
    print(diction)
