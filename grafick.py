import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

def graf(period_result, lenght, T1):
    x, y = lenght, period_result

    y = np.asarray(y[::-1])
    x = np.asarray(x[::-1])

    X_Y_Spline = make_interp_spline(x, y)

    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)

    fig, ax = plt.subplots(figsize=(10, 7), tight_layout=True)
    ax.plot(X_, Y_, label="Зависимость периода Т2 от расстояния между втулками")
    plt.axhline(T1, xmin=0, xmax=60, linestyle="--", c="green")

    plt.show()

def graf_2(period_result, lenght):
    y, x = period_result, lenght

    y = np.asarray(y)
    x = np.asarray(x)

    X_Y_Spline = make_interp_spline(x, y)

    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)

    fig, ax = plt.subplots(figsize=(10, 7), tight_layout=True)
    ax.plot(X_, Y_, label="Зависимость периода Т1 от расстояния между втулками")

    plt.show()
