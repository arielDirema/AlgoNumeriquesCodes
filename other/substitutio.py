"""
from typing import Callable, Tuple

def substitution_method(f: Callable[[float], float], g: Callable[[float], float], x0: float, tol: float = 1e-6, max_iter: int = 1000) -> Tuple[float, int]:
    """
"""
    Résolution de l'équation f(x) = 0 par la méthode de substitution x = g(x).

    :param f: La fonction f(x) dont on cherche la solution f(x) = 0.
    :param g: La fonction g(x) utilisée pour itérer xn+1 = g(xn).
    :param x0: Valeur initiale.
    :param tol: Tolérance pour la convergence. Doit être positive.
    :param max_iter: Nombre maximal d'itérations. Doit être positif.
    :return: La solution approximative x et le nombre d'itérations effectuées.
    :raise ValueError: Si tol ou max_iter sont négatifs ou nuls.
    :raise RuntimeError: Si la méthode de substitution n'a pas convergé après max_iter itérations.
    """
"""
    # Vérification des paramètres
    assert isinstance(f, Callable)
    assert isinstance(g, Callable)
    assert isinstance(x0, (int, float))
    assert isinstance(tol, (int, float))
    assert isinstance(max_iter, int)

    if tol <= 0 or max_iter <= 0:
        raise ValueError("tol et max_iter doivent être positifs")

    x = x0

    for iteration in range(max_iter):
        x_new = g(x)

        # Vérification de la convergence
        if abs(f(x_new)) < tol:
            return x_new, iteration

        x = x_new

    raise RuntimeError("La méthode de substitution n'a pas convergé après {} itérations.".format(max_iter))

# Exemple d'utilisation
if __name__ == "__main__":
    # Fonction f(x)
    def f(x: float) -> float:
        """
"""
        Fonction f(x) dont on cherche la solution f(x) = 0.
        """
"""
        return (x + 1)/(x - 1)

    # Fonction g(x)
    def g(x: float) -> float:
        """
"""
        Fonction g(x) utilisée pour itérer xn+1 = g(xn).
        """
"""
        return (x + 2) / (x + 1)

    # Valeur initiale
    x0 = 0.0

    # Résolution de l'équation f(x) = 0 par la méthode de substitution x = g(x)
    try:
        solution, itr = substitution_method(f, g, x0)
        print("Le nombre d'itération est :", itr)
        print("La solution de l'équation f(x) = 0 est :", solution)
    except Exception as e:
        print("Une erreur est survenue :", e)
"""

# Fonction f(x)
def f(x):
    return (x + 1) / (x - 1)

# Fonction g(x)
def g(x):
    return -0.5 * x - 1.5

# Valeur initiale
x0 = .0

# Tolérance pour la convergence
tol = 1e-6

# Nombre maximal d'itérations
max_iter = 1000

# Résolution de l'équation f(x) = 0 par la méthode de substitution x = g(x)
x = x0

for iteration in range(max_iter):
    x_new = g(x)

    # Vérification de la convergence
    if abs(f(x_new)) < tol:
        break

    x = x_new

# Affichage de la solution
print("x =", x)
print("f(x) =", f(x))
print("Nombre d'itérations :", iteration)
