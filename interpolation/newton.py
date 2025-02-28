import matplotlib.pyplot as plt
import numpy as np

def divided_difference(x_values, y_values):
    n = len(x_values)
    table = np.zeros((n, n))

    # Remplissage de la table de différences divisées
    for i in range(n):
        table[i, 0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x_values[i + j] - x_values[i])

    return table[0]

def newton_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    coefficients = divided_difference(x_values, y_values)

    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term

    return result

def plot_newton_interpolation(x_values, y_values, x_interpolate):
    interpolated_values = [newton_interpolation(x_values, y_values, x) for x in x_interpolate]

    plt.scatter(x_values, y_values, color='red', label='Points connus')
    plt.plot(x_interpolate, interpolated_values, color='blue', label='Interpolation de Newton')
    plt.title('Interpolation de Newton')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()







