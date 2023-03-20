def reading_data_1():
    with open('rezult1.txt', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()  # прочтение файла с результами измерений
        period_result = [float(item) for item in lines]

    length = [60 - 2 * i for i in range(0, 14)]
    T1 = float(input("Enter T1:"))

    return period_result, length, T1

def reading_data_2():
    with open('rezult2.txt', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()  # прочтение файла с результами измерений
        period_result = [float(item) for item in lines]

    length = [int(34 + 2 * i) for i in range(0, 14)]

    return period_result, length
