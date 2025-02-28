import numpy as np

# METHODE DE JACOBI
def jacobi(A, b, x0=None, tol=1e-6, max_iter=1000):
    n = len(b)
    x0 = x0 or np.zeros(n)

    for iteration in range(max_iter):
        x_new = np.zeros_like(x0)

        for i in range(n):
            sigma = A[i, :].dot(x0) - A[i, i] * x0[i]
            x_new[i] = (b[i] - sigma) / A[i, i]

        if np.linalg.norm(x_new - x0) < tol:
            return x_new, iteration

        x0 = x_new

    return 0
#METHODE DE JACOBI END

#METHODE DE GAUSS SEIDEL
def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=1000):
    
    n = len(b)
    x0 = x0 or np.zeros(n)

    for iteration in range(max_iter):
        x_new = np.zeros_like(x0)

        for i in range(n):
            sigma_before = A[i, :i].dot(x_new[:i])
            sigma_after = A[i, i+1:].dot(x0[i+1:])
            x_new[i] = (b[i] - sigma_before - sigma_after) / A[i, i]

        if np.linalg.norm(x_new - x0) < tol:
            return x_new, iteration

        x0 = x_new

    return 0
#METHODE DE GAUSS SEIDEL END
