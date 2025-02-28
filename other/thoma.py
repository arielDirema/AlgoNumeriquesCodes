def tridiagonal(M):
    rows, cols = len(M), len(M[0])

    # Vérifier si la matrice est carrée
    if rows != cols:
        return False

    # Vérifier si la matrice est tridiagonale
    for i in range(rows):
        for j in range(cols):
            if abs(i - j) > 1 and M[i][j] != 0:
                return False

    return True

def thomas_resolver(a, b, c, d):
    n = len(d)

    # Étape de factorisation
    for i in range(1, n):
        factor = a[i-1] / b[i-1]  # Correction ici
        b[i] -= factor * c[i-1]
        d[i] -= factor * d[i-1]

    # Étape de substitution rétrograde
    x = [0] * n
    x[-1] = d[-1] / b[-1]

    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

    return x

def thomas(M, B):
    if tridiagonal(M):
        # Récupérer les diagonales de la matrice M
        a = [M[i][i-1] for i in range(1, len(M))]
        b = [M[i][i] for i in range(len(M))]
        c = [M[i][i+1] for i in range(len(M)-1)]
        
        # Vérifier si les longueurs des diagonales sont correctes
        if len(a) != len(c) or len(b) != len(M):
            print("Erreur: Longueurs des diagonales incorrectes")
            return

        solution = thomas_resolver(a, b, c, B)
        print("Méthode de Thomas, la solution X =", solution)
        print("---------------------------------")
    else:
        print("La matrice n'est pas tridiagonale pour exécuter la méthode de Thomas")
        print("---------------------------------")

# Exemple d'utilisation
M = [
    [7, 2, 0, 0, 0],
    [1, 4, 3, 0, 0],
    [0, 5, 5, 1, 0],
    [0, 0, 1, 3, 2],
    [0, 0, 0, 1, 4]
]
B = [12, 0, 4, 3, 7]
thomas(M, B)
