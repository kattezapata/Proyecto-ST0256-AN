import numpy as np

def cholesky(A):
  n = A.shape[0]
  L = np.zeros((n, n), dtype=np.double)
  t=L.copy()
  cont=0
  for k in range(n): 
      L[k, k] = np.sqrt(A[k, k] - np.sum(L[k, :] ** 2))
    
      L[(k+1):, k] = (A[(k+1):, k] - L[(k+1):, :] @ L[:, k]) / L[k, k]
      
      d=np.linalg.norm(np.array(L)-np.array(t),np.inf)
      print("Para la iteración "+str(k+1)+": L = "+str(np.transpose(L.round(7)))+"\tError: "+str(abs(d)))
      U = np.transpose(L)
      cont=cont+1
    
  return L, U


#A = np.array([[2, -1, 0],[-1, 2, -1.], [0, -1, 2.]])
#L = cholesky(A)

#print("Solución: ")
#print(L)

#L = np.linalg.cholesky(A)
#print("Solución dada por numpy: ")
#print(L)