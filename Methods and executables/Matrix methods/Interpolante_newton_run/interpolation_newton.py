import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np
import math


#Newton Interpolation Method
def interpolation_newton(x,y):
    n = len(x)
    F = np.zeros((n,n))
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                F[j][i] = y[j]
            else:
                F[j][i] = (F[j][i-1] - F[j-1][i-1]) / (x[j]-x[j-i])
    return [F[a][a] for a in range(n)]