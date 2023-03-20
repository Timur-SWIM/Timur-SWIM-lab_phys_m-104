from grafick import graf, graf_2
from get_data import reading_data_1, reading_data_2
from calk import math
from writing_data import write_data

def main():
    period_result, length, T1 = reading_data_1()
    graf(period_result, length, T1)
    period_result, length = reading_data_2()
    graf_2(period_result, length)
    period_result, length, T1 = reading_data_1()
    g, d_g = math(period_result, length, T1)
    write_data(g, d_g)

if __name__ == '__main__':
    main()
