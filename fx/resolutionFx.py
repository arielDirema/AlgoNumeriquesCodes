import math

def dichotomie(f, a, b, epsilon):
    milieu = 0
    solution = 0
    solutions = []
    j = 0

    if a > b:
        print(f"Impossible de trouver la solution par la méthode de Dichotomie car a = {a:.2f} > {b:.2f} = b")
    else:
        if f(a) == 0:
            solution = a
            print(f"La solution  : {solution}  ", end="")
        elif f(b) == 0:
            solution = b
            print(f"La solution  : {solution}  ", end="")
        elif f(a) * f(b) < 0:
            while abs(b - a) > epsilon:
                milieu = (a + b) / 2
                if f(milieu) == 0:
                    solution = milieu
                    break
                elif f(a) * f(milieu) < 0:
                    b = milieu
                else:
                    a = milieu
                    solution = milieu
                    j += 1
            print(f"La solution  : {solution:.10f}  ", end="")
            print(f"Nombre d'iterations : {j}") 
        else:
            i = 0
            j = 0
            iters = []

            #if epsilon == 0:
            #    raise ValueError("Step size (epsilon) must be a non-zero value.")
            while(a < b):
                #print(a)
                #print(f(a))
                if f(a) < epsilon and f(a) > 0:
                    solutions.append(a)
                    iters.append(j)
                    i += 1
                a += epsilon
                j += 1

            if i > 0:
                #Apres segmentation de l'intervalle en de petits sous-intervalles,
                print(f"Il existe {i} solutions")
                taille = int(len(solutions)/2)
                print(f"x = {solutions[taille]:.10f}")
            else:
                #Apres segmentation de l'intervalle en de petits sous-intervalles
                print("il n'y a pas de solution")

def cordes(f, a, b, epsilon, max_iterations):
    """c = 0
    solution = 0
    solutions = []
    j = 0
    """
    x0 = a
    x1 = b

    if a > b:
        print(f"Impossible de trouver la solution car a = {a:.2f} > {b:.2f} = b")
    else:
            
        #La solution existe et est unique dans l'intervalle
        for i in range(max_iterations):
            f_x0 = f(x0)
            f_x1 = f(x1)

            if abs(f_x1 - f_x0) < epsilon:
                break  # La différence entre les valeurs de la fonction est suffisamment petite

            x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
            # Mettre à jour les points pour la prochaine itération
            x0 = x1 
            x1 = x_new

        print(f"La solution : {x1:.7f}  ", end="")
        print(f"Nombre d'iterations : {i}")

def newton_raphson(f, df, x, a, b, epsilon, max_iterations):
    x1 = x
    j = 0
    value = 0

    if a > b:
        print("Impossible de trouver la solution car a > b")
    else:
        x = x1
        x1 = x - (f(x) / df(x))
        while abs(x1 - x) > epsilon:
            if df(x) == 0:
                #Il y a divergence
                print("IMPOSSIBLE de trouver une solution.")
                break
            else:
                x = x1
                x1 = x - (f(x) / df(x))
            j += 1
            if j == max_iterations:
                value = 1
                break

        if not value:
            print(f"La solution : {x1:.7f}  ", end="")
            print(f"Nombre d'iterations : {j}")
        else:
            print(f"La solution n'existe pas (apres {iter} iterations).")

def substitution(f, g, x0, a, b, epsilon, max_iterations):
    #x = 0.5
    #x1 = g(x)
    #value = 0
    j = 0

    if a > b:
        print("Impossible de trouver la solution car a > b")
    else:
        x = x0
        for iteration in range(max_iterations):
            x1 = g(x)
            j += 1

            if abs(f(x1)) < epsilon:
                value = 1
                break

            x = x1

        if value:
            print(f"La solution : {x:.7f}  ", end="")
            print(f"Nombre d'iterations = {j}")
        else:
            print(f"La solution n'existe pas (apres {max_iterations} iterations).")


