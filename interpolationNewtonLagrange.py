from interpolation import plot_interpolations

import matplotlib.pyplot as plt
import numpy as np

# Interpolations de Newton et Lagrange avec fonction mère

def function(x):
    return x**3 + x**2 - 2*x

# Exemple d'utilisation
x_values = [-2.2, -2, -1, 0, 0.5, 1.5]
y_values = [-1.41, 0, 2, 0, -0.63, 2.63]
x_interpolate = np.linspace(min(x_values), max(x_values), 100)

# Tracer les courbes d'interpolation
plot_interpolations(x_values, y_values, x_interpolate, function)