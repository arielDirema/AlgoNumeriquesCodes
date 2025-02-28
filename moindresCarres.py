import numpy as np
import matplotlib.pyplot as plt

# Données d'exemple
x = np.array([-2.2,-2,-1,0,0.5,1.5])
y = np.array([-1.41,0,2,0,-0.63,2.63])

# Ajustement d'un polynôme de degré 2 (ajustez selon vos besoins)
coefficients = np.polyfit(x, y, 3)

# Création d'une fonction polynomiale
polynomial = np.poly1d(coefficients)

# Génération de points pour l'interpolation
x_interpolation = np.linspace(min(x), max(x), 100)
y_interpolation = polynomial(x_interpolation)

# Tracé des résultats
plt.scatter(x, y, label='Données')
plt.plot(x_interpolation, y_interpolation, label='Moindres carrés', color='red')
plt.legend()
plt.show()
       