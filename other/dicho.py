import numpy as np

# Exemple de matrice A et de vecteur b
A = np.array([[4, -1, 2],
              [-1, 5, 0],
              [2, 0, 6]])
b = np.array([12, -7, 4])

# Création de la matrice augmentée [A|b]
Ab = np.column_stack((A, b))


Ab = Ab.astype(np.float64)


# Fonction qui effectue la réduction de Gauss sur une matrice augmentée [A|b]
def gauss_reduction(Ab):
    n, m = Ab.shape
    for j in range(n):
        pivot = j
        for i in range(j + 1, n):
            if abs(Ab[i, j]) > abs(Ab[pivot, j]):
                pivot = i
        if pivot != j:
            Ab[[j, pivot]] = Ab[[pivot, j]]
        Ab[j] /= Ab[j, j]
        for i in range(n):
            if i != j:
                Ab[i] -= Ab[i, j] * Ab[j]
    return Ab

# Vérification si la matrice A est singulière
if np.linalg.det(A) == 0:
    print("La matrice A est singulière, on utilise la méthode du pseudo-inverse.")
    A_plus = np.linalg.pinv(A)
    x = A_plus @ (b - A @ (A_plus @ b))
else:
    print("La matrice A n'est pas singulière, on utilise la méthode de Gauss.")
    Ab = gauss_reduction(Ab.copy())  # Utilisez une copie pour éviter de modifier la matrice d'origine
    x = Ab[:, -1]

# Affichage de la solution
print("La solution du système Ax=b est:")
print(x)
