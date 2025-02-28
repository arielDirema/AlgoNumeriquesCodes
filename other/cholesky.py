# Ce programme résout un système d'équations linéaires Ax=b, par la méthode de Cholesky
# Il utilise la bibliothèque numpy pour manipuler les matrices et les vecteurs
import numpy as np

# Exemple de matrice A et de vecteur b
A = np.array([[4, 2],
               [2, 5]])
b = np.array([6, 7])

# Fonction qui effectue la décomposition de Cholesky sur une matrice symétrique et définie positive
def cholesky_decomposition(A):
    # Nombre de lignes et de colonnes de la matrice A
    n, m = A.shape
    # Vérification si la matrice est carrée
    if n != m:
        raise ValueError("La matrice n'est pas carrée")
    # Création d'une matrice L vide
    L = np.zeros((n, n))
    # Parcours des lignes de la matrice L
    for i in range(n):
        # Parcours des colonnes de la matrice L jusqu'à la diagonale
        for j in range(i + 1):
            # Calcul du terme L[i, j]
            if i == j:
                # Cas de la diagonale
                L[i, i] = np.sqrt(A[i, i] - np.sum(L[i, :i] ** 2))
            else:
                # Cas hors de la diagonale
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    # Retourne la matrice L
    return L

# Fonction qui résout un système triangulaire inférieur Lx = b
def forward_substitution(L, b):
    # Nombre de lignes et de colonnes de la matrice L
    n, m = L.shape
    # Vérification si la matrice est carrée
    if n != m:
        raise ValueError("La matrice n'est pas carrée")
    # Création d'un vecteur x vide
    x = np.zeros(n)
    # Parcours des lignes de la matrice L
    for i in range(n):
        # Calcul du terme x[i]
        x[i] = (b[i] - np.sum(L[i, :i] * x[:i])) / L[i, i]
    # Retourne le vecteur x
    return x

# Fonction qui résout un système triangulaire supérieur Ux = b
def backward_substitution(U, b):
    # Nombre de lignes et de colonnes de la matrice U
    n, m = U.shape
    # Vérification si la matrice est carrée
    if n != m:
        raise ValueError("La matrice n'est pas carrée")
    # Création d'un vecteur x vide
    x = np.zeros(n)
    # Parcours des lignes de la matrice U en sens inverse
    for i in range(n - 1, -1, -1):
        # Calcul du terme x[i]
        x[i] = (b[i] - np.sum(U[i, i + 1:] * x[i + 1:])) / U[i, i]
    # Retourne le vecteur x
    return x

# Vérification si la matrice A est symétrique
if np.allclose(A, A.T):
    # Si la matrice A est symétrique, on essaie la méthode de Cholesky
    try:
        # Application de la décomposition de Cholesky
        L = cholesky_decomposition(A)
        # Résolution du système Lz = b
        z = forward_substitution(L, b)
        # Résolution du système L.T x = z
        x = backward_substitution(L.T, z)
        # Affichage de la solution
        print("La solution du système Ax=b est:")
        print(x)
    except Exception as e:
        # Si la méthode de Cholesky échoue, on affiche l'erreur
        print("La méthode de Cholesky a échoué:")
        print(e)
else:
    # Si la matrice A n'est pas symétrique, on affiche un message
    print("La matrice A n'est pas symétrique, la méthode de Cholesky ne s'applique pas.")
