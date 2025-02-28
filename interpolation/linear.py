import matplotlib.pyplot as plt
import numpy as np

def linear_interpolation(x_values, y_values, x):

    """Interpolation linéaire.

    :param x_values: Liste des abscisses des points connus.
    :param y_values: Liste des ordonnées des points connus.
    :param x: Valeur à interpoler.
    :return: Valeur interpolée."""
    
    n = len(x_values)
    
    # Trouver les indices des points adjacents
    for i in range(n - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            # Calculer l'ordonnée interpolée
            slope = (y_values[i + 1] - y_values[i]) / (x_values[i + 1] - x_values[i])
            return y_values[i] + slope * (x - x_values[i])

    # Si x est en dehors de la plage des points connus, retourner None
    return None

def plot_linear_interpolation(x_values, y_values, x_interpolate):
    interpolated_values = [linear_interpolation(x_values, y_values, x) for x in x_interpolate]

    plt.scatter(x_values, y_values, color='red', label='Points connus')
    plt.plot(x_interpolate, interpolated_values, color='violet', label='Interpolation linéaire')
    plt.title('Interpolation linéaire')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

