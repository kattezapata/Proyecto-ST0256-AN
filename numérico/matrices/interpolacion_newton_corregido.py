import numpy as np

def interpolacion_newton(x,y):
    n = len(x)
    F = np.zeros((n,n))
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                F[j][i] = y[j]
            else:
                F[j][i] = (F[j][i-1] - F[j-1][i-1]) / (x[j]-x[j-i])
    return [F[a][a] for a in range(n)]

M = interpolacion_newton([1,1.2,1.4,1.6,1.8,2], [0.6747,0.8491,1.1214,1.4921,1.9607,2.5258])
print(M)
