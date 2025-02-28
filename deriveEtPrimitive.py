from sympy import symbols, log, exp, diff, integrate

# Définir la variable symbolique
x = symbols('x')

# Définir la fonction f(x)
f_x = x**3 - 2*x - 5

# Calculer la dérivée de f(x) par rapport à x
f_prime_x = diff(f_x, x)

# Afficher le résultat
print("Fonction originale f(x):", f_x)
print("Dérivée f'(x):", f_prime_x)


# Calculer la primitive de f(x) par rapport à x
primitive_f_x = integrate(f_x, x)

# Afficher le résultat
print("Primitive F(x):", primitive_f_x)