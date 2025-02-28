def methode_des_cordes(f, a, b, tol=1e-9, max_iter=100):
    """
    Méthode des cordes pour trouver une racine d'une fonction.

    :param f: La fonction dont on cherche la racine.
    :param a: Le début de l'intervalle.
    :param b: La fin de l'intervalle.
    :param tol: La tolérance pour arrêter l'itération.
    :param max_iter: Le nombre maximal d'itérations.
    :return: La valeur estimée de la racine.
    """
    x0, x1 = a, b

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < tol:
            break  # La différence entre les valeurs de la fonction est suffisamment petite

        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        # Mettre à jour les points pour la prochaine itération
        x0, x1 = x1, x_new

    return x1

# Exemple d'utilisation
if __name__ == "__main__":
    # Définir la fonction
    def f(x):
        return (x + 1) / (x - 1) 

    # Définir l'intervalle initial
    a = -2.0
    b = 2.0

    # Appeler la méthode des cordes
    root = methode_des_cordes(f, a, b)

    print("Racine trouvée:", root)
