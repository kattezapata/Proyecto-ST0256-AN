#This program finds the linear spline interpolating the given data using the
#linear plotter method.

#Inputs: 
#X, abscissae 
#Y, ordinates

#Outputs.
#Coef, coefficients of the tracers

import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np
import math



#Linear splines interpolation Method
def splines_linear(x,y):
    n = len(x)
    intervals=[]
    funtions=[]
    #y=mx+b
    for k in range(n-1):
      m=(y[k+1]-y[k])/(x[k+1]-x[k]) #Find m with points k and k+1
      b=y[k]-m*x[k] #Independent value
      if(b>0):
        fun='y = '+str(m)
        fun=fun+' x +'
        fun=fun+str(b)
        funtions.append(fun)#Line equation
      elif(b<0):
        fun='y = '+str(m)
        fun=fun+' x -'
        fun=fun+str(abs(b))
        funtions.append(fun)#Line equation
      else:
        fun='y = '+str(m)
        fun=fun+' x '
        funtions.append(fun)#Line equation
      interv='For x in [ '+str(x[k])
      interv=interv+' ,'
      interv=interv+str(x[k+1])
      interv=interv+' ]'
      intervals.append(interv)
     
    
        
    matr=[funtions,intervals]
    return matr


