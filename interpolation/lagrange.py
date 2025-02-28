import matplotlib.pyplot as plt
import numpy as np

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

def plot_lagrange_interpolation(x_values, y_values, x_interpolate):
    interpolated_values = [lagrange_interpolation(x_values, y_values, x) for x in x_interpolate]

    plt.scatter(x_values, y_values, color='red', label='Points connus')
    plt.plot(x_interpolate, interpolated_values, color='black', label='Interpolation de Lagrange')
    plt.title('Interpolation de Lagrange')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()





