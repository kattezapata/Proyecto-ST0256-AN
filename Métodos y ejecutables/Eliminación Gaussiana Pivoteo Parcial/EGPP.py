from numpy import array, zeros, fabs, linalg
import numpy as np

#a=array.input('Enter array A in []: ');
#b=array.input('Enter vector b in []: ');
#a = array([[[4,2,5],
# [2,5,8],
# [5,4,4,3]], float)

#b = array([[[60,70],
# [92.90],
# [56.30]], float)

#print("Solution by Numpy:")
#print(linalg.solve(a, b))

def EGPP(a,b):
  n = len(b)
  x = zeros(n, float)
  cont=0

  
  for k in range(n-1):
      if fabs(a[k][k]) < 1.0e-12:
          
          for i in range(k+1, n):
              if fabs(a[i][k]) > fabs(a[k][k]):
                  a[[k][i]] = a[[i][k]]
                  b[[k][i]] = b[[i][k]]
                  break
  
   
      for i in range(k+1,n):
          if a[i][k] == 0:continue
  
          factor = a[k][k]/a[i][k]
          for j in range(k,n):
              a[i][j] = a[k][j] - a[i][j]*factor
              
          b[i] = b[k] - b[i]*factor
          
  #return("Matríz resultado del proceso de Eliminación Gaussiana:")    
  #return(a)
  #return("Vector b:")
  #return(b)
  
  
  x[n-1] = b[n-1] / a[n-1][n-1]
  t=x.copy()
  for i in range(n-2, -1, -1):
      sum_ax = 0
    
      for j in range(i+1, n):
          sum_ax += a[i][j] * x[j]
          
      x[i] = (b[i] - sum_ax) / a[i][i]
      #d=np.linalg.norm(np.array(x)-np.array(t),np.inf)
      #print ("Para la iteración "+str(-(i-2))+": X = "+str(np.transpose(x.round(7)))+"\tError: "+str(abs(d)))
      cont=cont+1;
  
  #return("The solution of the system is:")
  return(x)
  #return("The number of iterations is: ")
  #return(cont)