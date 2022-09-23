def function_del():
    try:
        numb = int(input("Введите число:"))
    except ValueError:
        print("Ошибка типа данных...")
        return
    finally:
        print("конец")
        for i in range(1, numb + 1):
            if (numb % (i) == 0):
                print(i)
    return

function_del()
