# -*- coding: utf-8 -*-
"""Seidel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RGrRArUy65vDtKoq5zcQCfe6eg7awbkP
"""

import numpy as np
def seidel(A,B,x_0,tol,ite):
  p=np.shape(A)
  n=p[0]
  m=p[1]
  x=np.copy(x_0)
  dif = np.ones(n, dtype=float)
  error=tol*2
  it=0
  while not(error<=tol or it>ite):
    for i in range(0,n,1):
      sum=0
      for j in range(0,m,1):
        if(i!=j):
          sum=sum-A[i,j]*x[j]

      aux=(B[i]+sum)/A[i,i]
      dif[i]=np.abs(aux-x[i])
      x[i]=aux
    error=np.max(dif)
    it=it+1
  x=np.transpose([x])
  if (it>ite):
    x=0
  print('Vector solución')
  print(x)
  
A=np.array([[3. , -0.1, -0.2],
              [0.1,  7  , -0.3],
              [0.3, -0.2, 10  ]])

B=np.array([7.85,-19.3,71.4])
tol=0.00001
ite=100
x_0=[0.,0.,0.]
seidel(A,B,x_0,tol,ite)