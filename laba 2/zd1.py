def function_del():
    null = ''
    try:
        numb = int(input("Введите число:"))
    except ValueError:
        print("Ошибка типа данных!1!!!111111!!!")
        return
    for i in range(numb//2 + 1):
        if (numb % (i + 1) == 0):
            print(i + 1)
    return null
function_del()
