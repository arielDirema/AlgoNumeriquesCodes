from fx import substitution
from fx import dichotomie
from fx import newton_raphson
from fx import cordes

def f(x):
    return x**3 - 2*x - 5
def df(x):
    return 3*x**2 - 2
def g(x):
    return (2*x + 5)**(1/3) 

if __name__ == "__main__":
    a = 1
    b = 4
    x = 1.5
    epsilon = 10**-6
    max_iterations = 1000
    print("FONCTION : x**3 - 2*x - 5")
    print("\n")
    print("--------------- DICHOTOMIE --------------- ")
    dichotomie(f, a, b, epsilon)
    print("\n")

    print("--------------- NEWTON RAPHSON --------------- ")
    newton_raphson(f, df, x, a, b, epsilon, max_iterations)
    print("\n")

    print("--------------- SUBSTITUTION --------------- ")
    substitution(f, g, x, a, b, epsilon, max_iterations)
    print("\n")

    print("--------------- CORDES --------------- ")
    cordes(f, a, b, epsilon, max_iterations)
    print("\n")
    
    
    

