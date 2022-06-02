import numpy as np
def seidel(A,b,x0,tol,ite):
  [m,n]=np.shape(A)
  k=0
  error=[]
  comp=np.zeros(m)
  while k<ite:
    k+=1
    sum=0
    for i in range(0,m):
      sum=0
      for j in range(0,n):
        if (j!=i):
         sum=sum+A[i,j]*x0[j]
      x0[i]=(b[i]-sum)/A[i,i]
      #print("x["+str(i+1)+"]:"+ str(x0[1]))
    del error[:]
    for i in range(0,m):
      sum=0
      for j in range(0,n):
         sum=sum+A[i,j]*x0[j]
      comp[i]=sum
      dif=comp[i]-b[i]
      error.append(dif)
    if all(i<=tol for i in error)==True:
      break
  return x0, error
