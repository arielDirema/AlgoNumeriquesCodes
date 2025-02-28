# Ce programme résout un système d'équations linéaires Ax=b, par la méthode de Gauss
# Il utilise la bibliothèque numpy pour manipuler les matrices et les vecteurs
import numpy as np

# Exemple de matrice A et de vecteur b
A = np.array([[1, 1, 1],
                          [2, 2, 5],
                          [4, 6, 8]])
b = np.array([1, 2, 5])

# Fonction qui effectue la réduction de Gauss sur une matrice augmentée [A|b]
def gauss_reduction(Ab):
    # Nombre de lignes et de colonnes de la matrice augmentée
    n, m = Ab.shape
    # Parcours des colonnes de la matrice A
    for j in range(n):
        # Recherche du pivot maximal dans la colonne j
        pivot = j
        for i in range(j + 1, n):
            if abs(Ab[i, j]) > abs(Ab[pivot, j]):
                pivot = i
        # Echange des lignes j et pivot si nécessaire
        if pivot != j:
            Ab[[j, pivot]] = Ab[[pivot, j]]
        # Division de la ligne j par le pivot
        Ab[j] = Ab[j] / Ab[j, j]
        # Elimination des coefficients non nuls dans les autres lignes
        for i in range(n):
            if i != j:
                Ab[i] = Ab[i] - Ab[i, j] * Ab[j]
    # Retourne la matrice réduite
    return Ab

# Création de la matrice augmentée [A|b]
Ab = np.hstack((A, b.reshape(-1, 1)))

# Application de la réduction de Gauss
Ab = gauss_reduction(Ab)

# Extraction de la solution x
x = Ab[:, -1]

# Affichage de la solution
print("La solution du système Ax=b est:")
print(x)

"""

# Ce programme résout un système d'équations linéaires Ax=b, par la méthode de Gauss
# Il utilise la bibliothèque numpy pour manipuler les matrices et les vecteurs
import numpy as np

# Exemple de matrice A et de vecteur b
A = np.array([[1, 1, 1],
                [2, 2, 5],
                [4, 6, 8]])
b = np.array([1, 2, 5])

# Fonction qui effectue la réduction de Gauss sur une matrice augmentée [A|b]
def gauss_reduction(Ab):
    # Nombre de lignes et de colonnes de la matrice augmentée
    n, m = Ab.shape
    # Parcours des colonnes de la matrice A
    for j in range(n):
        # Recherche du pivot maximal dans la colonne j
        pivot = j
        for i in range(j + 1, n):
            if abs(Ab[i, j]) > abs(Ab[pivot, j]):
                pivot = i
        # Echange des lignes j et pivot si nécessaire
        if pivot != j:
            Ab[[j, pivot]] = Ab[[pivot, j]]
        # Division de la ligne j par le pivot
        Ab[j] = Ab[j] / Ab[j, j]
        # Elimination des coefficients non nuls dans les autres lignes
        for i in range(n):
            if i != j:
                Ab[i] = Ab[i] - Ab[i, j] * Ab[j]
    # Retourne la matrice réduite
    return Ab

# Création de la matrice augmentée [A|b]
Ab = np.hstack((A, b.reshape(-1, 1)))

# Vérification si la matrice A est singulière
if np.linalg.det(A) == 0:
    # Si la matrice A est singulière, on utilise la méthode du pseudo-inverse
    print("La matrice A est singulière, on utilise la méthode du pseudo-inverse.")
    # Calcul du pseudo-inverse de A
    A_plus = np.linalg.pinv(A)
    # Calcul de la solution x
    x = A_plus.dot(b - A.dot(A_plus.dot(b)))
else:
    # Si la matrice A n'est pas singulière, on utilise la méthode de Gauss
    print("La matrice A n'est pas singulière, on utilise la méthode de Gauss.")
    # Application de la réduction de Gauss
    Ab = gauss_reduction(Ab)
    # Extraction de la solution x
    x = Ab[:, -1]

# Affichage de la solution
print("La solution du système Ax=b est:")
print(x)"""

