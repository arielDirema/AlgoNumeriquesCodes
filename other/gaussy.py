def gaussian_elimination(A, b):
    """
    Résolution d'un système d'équations linéaires Ax = b par la méthode de Gauss.

    :param A: Matrice des coefficients du système.
    :param b: Vecteur des termes constants.
    :return: Vecteur solution x.
    """
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

# Exemple d'utilisation
if __name__ == "__main__":
    A = [[7, 2, 0, 0, 0],
         [2, 4, 1, 0, 0],
         [0, 1, 5, 3, 0],
         [0, 0, 3, 5, 1],
         [0, 0, 0, 1, 4]]

    b = [12, 0, 4, 3, 7]

    solution = gaussian_elimination(A, b)
    print("\n")
    print("--------------- THOMAS ---------------")
    solution = gaussian_elimination(A, b)
    print(f"la solution : {solution}")
    print("\n")