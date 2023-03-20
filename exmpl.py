import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset
x = [60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34]
x_rev = np.array(x[::-1])
y = [1.385, 1.369, 1.345, 1.338, 1.334, 1.329, 1.327, 1.336, 1.353, 1.362, 1.430, 1.461, 1.593, 1.787]
y_rev = np.array(y[::-1])

X_Y_Spline = make_interp_spline(x_rev, y_rev)

X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# Plotting the Graph
plt.plot(X_, Y_)
plt.title("Curve plotted using the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()