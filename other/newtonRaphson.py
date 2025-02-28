def newton_raphson(f, df, x0, tol=1e-9, max_iter=100):
    """
    Méthode de Newton-Raphson pour trouver une racine d'une fonction.

    :param f: La fonction dont on cherche la racine.
    :param df: La dérivée de la fonction.
    :param x0: L'estimation initiale de la racine.
    :param tol: La tolérance pour arrêter l'itération.
    :param max_iter: Le nombre maximal d'itérations.
    :return: La valeur estimée de la racine.
    """
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise RuntimeError("La méthode de Newton-Raphson n'a pas convergé après {} itérations.".format(max_iter))

# Exemple d'utilisation
if __name__ == "__main__":
    # Définir la fonction et sa dérivée
    def f(x):
        return (x + 1)/(x - 1)

    def df(x):
        return -2/(x - 1)**2

    # Estimation initiale
    x0 = 2.0

    # Appeler la méthode de Newton-Raphson
    root = newton_raphson(f, df, x0)

    print("Racine trouvée:", root)
