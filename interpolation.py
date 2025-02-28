from interpolation import plot_lagrange_interpolation
from interpolation import plot_linear_interpolation
from interpolation import plot_newton_interpolation

import matplotlib.pyplot as plt
import numpy as np

# Exemple d'utilisation
x_values = [-1.5,-1,0,1,2,2.5]
y_values = [-53/8,-6,-7,-6,3,99/8]

#LAGRANGE

# Générer des valeurs pour l'interpolation
x_interpolate = np.linspace(min(x_values), max(x_values), 100)
# Tracer la courbe interpolée
plot_lagrange_interpolation(x_values, y_values, x_interpolate)


#LINEAR

# Générer des valeurs pour l'interpolation
x_interpolate = np.linspace(min(x_values), max(x_values), 100)
# Tracer la courbe interpolée
plot_linear_interpolation(x_values, y_values, x_interpolate)


#NEWTON

# Générer des valeurs pour l'interpolation
x_interpolate = np.linspace(min(x_values), max(x_values), 100)
# Tracer la courbe interpolée
plot_newton_interpolation(x_values, y_values, x_interpolate)







