import numpy as np
#Full pivot Method
def full_pivot(A,B):

    m,n=np.shape(A)
    B = np.split(B,np.size(B))
    AB = np.append(A,B,axis=1)
    brand = np.arange(n)
    brand = np.split(brand,np.size(brand))

    for i in range(m):
        a = A[i:,i:]
        f,c = np.where(A == np.max(np.abs(a)))
        f = f[0]
        c = c[0]

        aux1 = np.copy(AB[i])
        AB[i] = AB[f]
        AB[f] = aux1
        aux1 = np.copy(AB[:,i])

        b = np.copy(brand[i])
        brand[i] = brand[c]
        brand[c] = b

        AB[:,i] =AB[:,c]
        AB[:,c] =aux1
        pivot = AB[i,i]
        aux2 = AB[i]/pivot
        AB[i] = aux2

        for j in range(i+1,m):
            r = AB[j][i]
            AB[j] = AB[j]-AB[i]*r

    for k in range(m-1):
        for h in range(m-1):
            r = AB[m-h-k-2][m-k-1]
            AB[m-h-2-k] = AB[m-h-2-k]-AB[m-k-1]*r

    x = np.arange(n,dtype=float)
    for l in range(n):
        p = brand[l][0]
        x[p] = (AB[l][n])

    return x