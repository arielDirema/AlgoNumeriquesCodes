import numpy as np

def crout_solve(A, b):
    n = len(b)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # Décomposition de Crout
    for k in range(n):
        # Calcul de la partie supérieure (U)
        for j in range(k, n):
            U[k, j] = A[k, j] - sum(L[k, i] * U[i, j] for i in range(k))

        # Calcul de la partie inférieure (L)
        for i in range(k, n):
            L[i, k] = (A[i, k] - sum(L[i, j] * U[j, k] for j in range(k))) / U[k, k]

    # Étape 2: Résoudre Ly = b
    y = np.linalg.solve(L, b)

    # Étape 3: Résoudre Ux = y
    x = np.linalg.solve(U, y)

    return x

# Exemple d'utilisation
if __name__ == "__main__":
    A = np.array([[4, -1, 2],
                [-1, 5, 0],
                [2, 0, 6]])

    b = np.array([12, -7, 4])

    det_A = np.linalg.det(A)

    if np.isclose(det_A, 0):
        print("La matrice A est singulière.")
    else:
        # Utiliser la fonction crout_solve pour résoudre le système
        solution = crout_solve(A, b)

        print("La solution du système avec la décomposition de Crout est :", solution)
    


