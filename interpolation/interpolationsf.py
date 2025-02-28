import matplotlib.pyplot as plt
import numpy as np

def lagrange_interpolation(x_values, y_values, x):
    """
    Interpolation de Lagrange.

    :param x_values: Liste des abscisses des points connus.
    :param y_values: Liste des ordonnées des points connus.
    :param x: Valeur à interpoler.
    :return: Valeur interpolée.
    """
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

def linear_interpolation(x_values, y_values, x):
   
    n = len(x_values)

    # Trouver les indices des points adjacents
    for i in range(n - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            # Calculer l'ordonnée interpolée
            slope = (y_values[i + 1] - y_values[i]) / (x_values[i + 1] - x_values[i])
            return y_values[i] + slope * (x - x_values[i])

    # Si x est en dehors de la plage des points connus, retourner None
    return None

def divided_difference(x_values, y_values):
    """
    Calcule les différences divisées nécessaires pour l'interpolation de Newton.

    :param x_values: Liste des abscisses des points connus.
    :param y_values: Liste des ordonnées des points connus.
    :return: Liste des coefficients de différences divisées.
    """
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
    """
    Interpolation de Newton.

    :param x_values: Liste des abscisses des points connus.
    :param y_values: Liste des ordonnées des points connus.
    :param x: Valeur à interpoler.
    :return: Valeur interpolée.
    """
    n = len(x_values)
    result = 0.0
    coefficients = divided_difference(x_values, y_values)

    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term

    return result

# Interpolations de Newton et Lagrange avec fonction mère
def plot_interpolations(x_values, y_values, x_interpolate, function):

    linear_values = [linear_interpolation(x_values, y_values, x) for x in x_interpolate]
    newton_values = [newton_interpolation(x_values, y_values, x) for x in x_interpolate]
    lagrange_values = [lagrange_interpolation(x_values, y_values, x) for x in x_interpolate]

    x_original = np.linspace(min(x_values), max(x_values), 100)
    y_original = [function(x) for x in x_original]

    plt.plot(x_original, y_original, color='violet', label='Fonction mère', linestyle='dashed')
    plt.scatter(x_values, y_values, color='red', label='Points connus')


    plt.plot(x_interpolate, newton_values, 'r.', label='Interpolation de Newton')
    plt.plot(x_interpolate, lagrange_values, 'b-.', label='Interpolation de Lagrange')

    plt.title('Interpolations de Newton et Lagrange avec fonction mère')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

