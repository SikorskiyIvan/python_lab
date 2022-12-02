import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def print_menu():
    print("\n 1. Проверить на пропуски и аномальные значения\n"
          " 2. Проверить на нормальность распределения и выбросы\n"
          " 3. Определить количество квартир с уникальной жилой площадью\n"
          " 4. Построить сводную таблицу\n"
          " 5. Выход")

def check_null(price_prepared):
    for col, dat in rslt_b.items():
        skip = rslt_b[rslt_b[col].isnull()]
        if not skip.empty:
            print(f"В {col} столбце были найдены пропуски")
            for col_name, data in b.items():
                skips = rslt_b[rslt_b[col_name].isnull()]
                if not skips.empty:
                    rslt_b[col_name] = input(f"Чем заменить пропуски в {col_name}:")

def boxplot_and_barchart(price_prepared):
    entered_graf = int(input(" 1. Ящик с усами\n 2. Гистограмма\n"))
    if entered_graf == 1:
        rslt_b.plot(kind='box')
        plt.semilogy()
    elif entered_graf == 2:
        square = rslt_b['Square']
        price = rslt_b['Price']
        fig = plt.figure(figsize=(10, 7))
        plt.bar(square[0:10], price[0:10])
    plt.show()

def pivot_table(price_prepared):
    book_info = pd.pivot_table(rslt_b, values='m_sq', index=['LifeSquare'], columns=['Price'], aggfunc=np.sum, fill_value=0)
    print(f"Сводная таблица:\n{book_info}")
    rslt_b.to_csv("surname.csv")


b = pd.read_csv("price_prepared.csv", sep = ";")
b.head(1000)
rslt_b = b[(b['Square'] > 0) & (b['LifeSquare'] > 0) & (b['KitchenSquare'] > 0) & (b['m_sq'] > 0)]
while True:
    print_menu()
    try:
        while True:
            choice = int(input("Выберите операцию: "))
            if 6 < choice < 1:
                raise ValueError
            match choice:
                case 1:
                    check_null(rslt_b)
                    print("Датасет без аномальных значений:\n", rslt_b)
                    break
                case 2:
                    boxplot_and_barchart(rslt_b)
                    break
                case 3:
                    unique_b = rslt_b["LifeSquare"].value_counts()
                    print(unique_b)
                    break
                case 4:
                    pivot_table(rslt_b)
                    break
                case 5:
                    print("До свидания!")
                    exit(0)
    except ValueError:
        print("Некорректный ввод!")
