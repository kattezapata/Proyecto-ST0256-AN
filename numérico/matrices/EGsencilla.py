import numpy as np

def gaussiana_sencilla(M):
    n = len(M)
    M = M.astype('float64')
    for i in range(n):
        for j in range(n-1, i, -1):
            M[j] = M[j] - M[i]*(M[j][i]/M[i][i])
    return M

