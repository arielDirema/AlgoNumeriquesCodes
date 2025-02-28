def dichotomie(f, a, b, tol=1e-9, max_iter=100):
    """
    Méthode de dichotomie pour trouver une racine d'une fonction.

    :param f: La fonction dont on cherche la racine.
    :param a: Le début de l'intervalle.
    :param b: La fin de l'intervalle.
    :param tol: La tolérance pour arrêter l'itération.
    :param max_iter: Le nombre maximal d'itérations.
    :return: La valeur estimée de la racine.
    """
    if f(a) * f(b) > 0:
        raise ValueError("La fonction ne change pas de signe sur l'intervalle donné.")

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        if abs(b - a) < tol or fc == 0:
            return c
        elif f(a) * fc < 0:
            b = c
        elif f(b) * fc < 0:
            a = c
        else:
            raise ValueError("La fonction a une singularité ou un point d'indétermination.")

    raise RuntimeError("La méthode de dichotomie n'a pas convergé après {} itérations.".format(max_iter))

# Exemple d'utilisation
if __name__ == "__main__":
    # Définir la fonction
    def f(x):
        if x == 1:
            return float('inf')  # Évite la division par zéro
        return (x + 1) / (x - 1)

    # Définir l'intervalle initial
    a = 1.0
    b = 2.0

    root = dichotomie(f, a, b)
    print("Racine trouvée:", root)
    


    """
    try:
        # Appeler la méthode de dichotomie
        root = dichotomie(f, a, b)
        print("Racine trouvée:", root)
    except ValueError as ve:
        print("Erreur de valeur:", ve)
    except RuntimeError as re:
        print("Erreur d'exécution:", re)
    """
