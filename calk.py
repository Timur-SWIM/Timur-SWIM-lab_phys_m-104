def math(period_result, lenght, T1):
    l = float(input("Enter Lпр:"))
    g = math_g(T1)
    d_t = math_d_t(period_result)
    d_g = math_d_g(T1,d_t, l, g)
    return g, d_g


def math_g(T1):
    l = float(input("Enter Lпр:"))
    Pi = 3.14159
    g = round(((((2 * Pi) / T1) ** 2) * l), 3)
    return g


def math_d_t(period_result):
    t_ = round(((sum(period_result)) / len(period_result)), 2)
    delta_t2 = [round((period_result[i] - t_) ** 2, 3) for i in range(len(period_result))]
    sigma = round((sum(delta_t2) / 49) ** 0.5, 2)
    d_t = 2 * sigma
    return d_t

def math_d_g(t, d_t, l, g):
    d_g = round(g * ((((d_t ** 2/t ** 2) ** 2) + l ** 2) ** 0.5),3)
    return d_g
