import numpy as np

# FACTORIZACIÓN LU SENCILLA
def lu(M):
    n = len(M)
    U = M.astype('float64')
    L = np.eye(n).astype('float64')
    for i in range(n):
        for j in range(n-1, i, -1):
            L[i][j] = (U[j][i]/U[i][i])
            U[j] = U[j] - U[i]*(U[j][i]/U[i][i])
    L = L.T
    return L, U 

# FACTORIZACIÓN LU CON PIVOTEO PARCIAL
def lu_pivoteo_parcial(M):
    n = len(M)
    U = M.astype('float64')
    L = np.eye(n).astype('float64')
    P = np.eye(n)
    for i in range(n):
        for j in range(n-1, i, -1):
            max_index = indexOfMax(U.T[i])
            if max_index > i:
                temp1 = np.copy(U[i])
                temp2 = np.copy(P[i])
                U[i] = U[max_index]
                P[i] = P[max_index]
                U[max_index] = temp1
                P[max_index] = temp2
            L[i][j] = (U[j][i]/U[i][i])
            U[j] = U[j] - U[i]*(U[j][i]/U[i][i])
    L = L.T
    return L, U, P

def indexOfMax(arr):
    index = 0
    for i in range(len(arr)):
        if abs(arr[i]) > abs(arr[index]):
            index = i
    return index
