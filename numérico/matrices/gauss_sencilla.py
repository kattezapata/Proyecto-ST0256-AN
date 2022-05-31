import numpy as np

def gaussiana_sencilla(M):
    n = len(M)
    M = M.astype('float64')
    for i in range(n):
        for j in range(n-1, i, -1):
            M[j] = M[j] - M[i]*(M[j][i]/M[i][i])
    return M

matrix = np.array([[4,3,-2,-7],[3,12,8,-3],[2,3,-9,3],[1,-2,-5,6]])
M = gaussiana_sencilla(matrix)
print(M)
