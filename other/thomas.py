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
        factor = a[i - 1] / b[i - 1]
        b[i] -= factor * c[i - 1]
        d[i] -= factor * d[i - 1]

    # Étape de substitution rétrograde
    x = [0] * n
    x[-1] = d[-1] / b[-1]

    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

    return x

def thomas(M,B):
    if(tridiagonal(M)):
        a = [0, 2, 1, 3, 1] #diagonale inferieure
        b = [7, 4, 5, 5, 4] #diagonale principale
        c = [2, 1, 3, 1, 0] #diagonale superieure
        d = [12, 0, 4, 3, 7] # Terme constant
        solution = thomas_resolver(a, b, c, d)
        print("Methode de Thomas la solution X = ", solution)
        print("---------------------------------")
    else:
        print("La matrice n'est pas tridiagonale pour executer la methode de thomas")
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