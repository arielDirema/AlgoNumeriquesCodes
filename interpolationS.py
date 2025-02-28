from interpolation import plot_interpolation

import numpy as np
import matplotlib.pyplot as plt

# Exemple d'utilisation
x_values = [-2.2,-2,-1,0,0.5,1.5]
y_values = [-1.41,0,2,0,-0.63,2.63]

x_interpolate = np.linspace(min(x_values), max(x_values), 100)
# Tracer la courbe interpolée
plot_interpolation(x_values, y_values, x_interpolate)