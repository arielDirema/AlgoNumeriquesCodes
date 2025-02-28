import numpy as np

from ax import gauss
from ax import gauss_jordan
from ax import cholesky
from ax import crout
from ax import gauss_seidel
from ax import jacobi
from ax import matrix_is_positive


# Demander à l'utilisateur d'entrer l'ordre de la matrice
"""n = int(input("Entrez l'ordre de la matrice: "))

# Initialiser la matrice avec des zéros
A = np.zeros((n, n))
b = np.zeros(n)

# Demander à l'utilisateur d'entrer les éléments de la matrice
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Entrez l'élément A[{i+1}, {j+1}] : "))

for i in range(n):
    b[i] = float(input(f"Entrez l'élément b[{i+1}]: "))"""


A = np.array([[7, 2, 0, 0, 0],
              [2, 4, 1, 0, 0],
              [0, 1, 5, 3, 0],
              [0, 0, 3, 5, 1],
              [0, 0, 0, 1, 4]])

b = np.array([12, 0, 4, 3, 7])


# Afficher la matrice
print("--------------- Matrice A --------------- ")
print(A)
print("--------------- Matrice b --------------- ")
print(b)
print("\n")

#APPEL DES METHODES DIRECTES
print("--------------- METHODES DIRECTES --------------- ")
#APPEL DE LA METHODE DE GAUSS
"""
print("--------------- GAUSS ---------------")
s_g = gauss(A, b)
print(f"la solution : {s_g}")
print("\n")"""

#APPEL DE LA METHODE DE GAUSS JORDAN
print("--------------- GAUSS JORDAN ---------------")
s_gj = gauss_jordan(A, b)
print(f"la solution : {s_gj}")
print("\n")

#APPEL DE LA METHODE DE CROUT
print("--------------- CROUT ---------------")
s_c = crout(A, b)
print(f"la solution : {s_c}")
print("\n")

#APPEL DE LA METHODE DE CHOLESKY
print("--------------- CHOLESKY ---------------")
if(matrix_is_positive(A)):
    s_ch = cholesky(A, b)
    print(f"la solution : {s_ch}")
    print("\n")
else:
    print("la matrice n'est pas symetrique definie positive")
    print("\n")


#APPEL DES METHODES INDIRECTES
print("--------------- METHODES INDIRECTES --------------- ")
#APPEL DE LA METHODE DE JACOBI
print("--------------- JACOBI ---------------")
if jacobi(A, b) == 0:
    print("La méthode de Jacobi n'a pas convergé après 1000 itérations.")
else:
    s_j, i = jacobi(A, b)
    print(f"la solution : {s_j}")
    print(f"Nombre d'itérations : {i}")
    print("\n")

#APPEL DE LA METHODE DE GAUSS SEIDEL
print("--------------- GAUSS SEIDEL ---------------")
if gauss_seidel(A, b) == 0:
    print("La méthode de Gauss-Seidel n'a pas convergé après 1000 itérations.")
else:
    s_gs, i = gauss_seidel(A, b)
    print(f"la solution : {s_gs}")
    print(f"Nombre d'itérations : {i}")


