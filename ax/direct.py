import numpy as np

#METHODE GAUSS START
def gauss(A, b):
    
    n = len(b)

    # Étape 1: Construction de la matrice augmentée [A|b]
    augmented_matrix = [row + [bi] for row, bi in zip(A, b)]

    # Étape 2: Élimination vers le haut
    for i in range(n):
        # Recherche du pivot
        max_row = max(range(i, n), key=lambda k: abs(augmented_matrix[k][i]))
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        # Normalisation de la ligne
        pivot = augmented_matrix[i][i]
        augmented_matrix[i] = [elem / pivot for elem in augmented_matrix[i]]

        # Élimination
        for j in range(i + 1, n):
            factor = augmented_matrix[j][i]
            augmented_matrix[j] = [elem_j - factor * elem_i for elem_i, elem_j in zip(augmented_matrix[i], augmented_matrix[j])]

    # Étape 3: Rétro-substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i][-1] - sum(augmented_matrix[i][j] * x[j] for j in range(i + 1, n))

    return x
#END METHODE GAUSS

#METHODE DE GAUSS_JORDAN
def gauss_jordan(A, b):
    n = len(b)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)
    Ab = Ab.astype(float)
    for i in range(n):
        # Find pivot row
        pivot = i
        for j in range(i + 1, n):
            if abs(Ab[j, i]) > abs(Ab[pivot, i]):
                pivot = j
        # Swap pivot row with current row
        Ab[[i, pivot]] = Ab[[pivot, i]]
        # Normalize pivot row
        Ab[i] /= Ab[i, i]
        # Eliminate other rows
        for j in range(n):
            if j != i:
                Ab[j] -= Ab[j, i] * Ab[i]
    return Ab[:, n]
#END METHODE DE GAUSS_JORDAN

#METHODE DE CHOLESKY START
def matrix_is_positive(matrix):
    try:
        np.linalg.cholesky(matrix)
        return True
    except np.linalg.LinAlgError:
        return False

def decomposition(A):
    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i][j] = np.sqrt(A[i][i] - sum(L[i][k] ** 2 for k in range(j)))
            else:
                L[i][j] = (A[i][j] - sum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]

    return L

def cholesky(A, b):
    """
    Résolution d'un système d'équations linéaires Ax = b par la méthode de Cholesky.

    :param A: Matrice symétrique définie positive des coefficients du système.
    :param b: Vecteur des termes constants.
    :return: Vecteur solution x.
    """
    L = decomposition(A)
    print("La matrice L est :")
    print(L)

    # Résolution de Ly = b par substitution avant
    y = np.linalg.solve(L, b)

    # Résolution de L^T x = y par substitution arrière
    x = np.linalg.solve(L.T, y)

    return x
#METHODE DE CHOLESKY END

#METHODE DE CROUT LU
def crout_decomposition(A):
    if np.linalg.det(A) == 0:
        print("La matrice A est singulière.")
    else:
        n = len(A)
        L = np.zeros((n, n))
        U = np.zeros((n, n))

        for i in range(n):
            # Calcul des éléments de la matrice U
            for j in range(i, n):
                U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

            # Calcul des éléments de la matrice L
            for j in range(i, n):
                if i == j:
                    L[i][j] = 1
                else:
                    L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

        return L, U

def crout(A, b):
    L, U = crout_decomposition(A)
    print("La matrice L est :")
    print(L)
    print("La matrice U est :")
    print(U)
    
    if np.linalg.det(L) == 0:
        print("La matrice L est singulière")
    elif np.linalg.det(U) == 0:
        print("La matrice U est singulière")
    else:
        # Résolution de Ly = b par substitution avant
        y = np.linalg.solve(L, b)

        # Résolution de Ux = y par substitution arrière
        x = np.linalg.solve(U, y)

        return x
#METHODE DE CROUT LU END


