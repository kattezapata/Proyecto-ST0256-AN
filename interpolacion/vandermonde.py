import numpy as np

def vandermonde(x,y):
    n = len(x)
    M = np.zeros((n,n))
    for i in range(len(x)):
        for j in range(len(x)):
            M[i][j] = x[i]**j
    return np.linalg.inv(M) @ y
