#This program finds the cuadratic spline interpolating the given data.



import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np
import math



#Cuadratic splines interpolation Method
def splines_cuadratic(x,y):
    n = len(x)
    intervals=[]
    funtions=[]
    #y=mx+b
    #first interval
    m=(y[1]-y[0])/(x[1]-x[0]) #Find m with points k and k+1
    b=y[0]-m*x[0] #Independent value
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
    interv='For x in [ '+str(x[0])
    interv=interv+' ,'
    interv=interv+str(x[1])
    interv=interv+' ]'
    intervals.append(interv)
    
    
    for k in range(1, n-2): # k:_0, k+1:_1, k+2:_2
      m1=(y[k+1]-y[k])/(x[k+1]-x[k]) #Find m with points k and k+1
      m2=(y[k+2]-y[k+1])/(x[k+2]-x[k+1]) #Find m with points k+1 and k+2
      c=(m2-m1)/(x[k+2]-x[k]) #x^2
      b2=y[k]-m1*x[k] +(c*x[k]*x[k+1])#Independent value b
      a=m1-(x[k+1]*c)-(c*x[k])  #x
      #b2 independent value
      if(b2>0 and a>0):
        fun2='y = '+str(c)
        fun2=fun2+' x^2 + '
        fun2=fun2+str(a)
        fun2=fun2+' x +'
        fun2=fun2+str(b2)
        funtions.append(fun2)#Line equation
      elif(b2<0 and a>0):
        fun2='y = '+str(c)
        fun2=fun2+' x^2 + '
        fun2=fun2+str(a)
        fun2=fun2+' x -'
        fun2=fun2+str(abs(b2))
        funtions.append(fun2)#Line equation
      elif(b2>0 and a<0):
        fun2='y = '+str(c)
        fun2=fun2+' x^2 - '
        fun2=fun2+str(abs(a))
        fun2=fun2+' x +'
        fun2=fun2+str(b2)
        funtions.append(fun2)#Line equation
      elif(b2<0 and a<0):
        fun2='y = '+str(c)
        fun2=fun2+' x^2 - '
        fun2=fun2+str(abs(a))
        fun2=fun2+' x -'
        fun2=fun2+str(abs(b2))
        funtions.append(fun2)#Line equation  
      elif(a==0 and b2>0):
        fun2='y = '+str(c)
        fun2=fun2+' x^2 + '
        fun2=fun2+str(abs(b2))
        funtions.append(fun2)#Line equation  
      elif(a==0 and b2<0):
        fun2='y = '+str(c)
        fun2=fun2+' x^2 - '
        fun2=fun2+str(abs(b2))
        funtions.append(fun2)#Line equation    
      elif(b2==0 and a>0):
        fun2='y = '+str(c)
        fun2=fun2+' x^2 + '
        fun2=fun2+str(a)
        fun2=fun2+' x'
        funtions.append(fun2)#Line equation    
      elif(b2==0 and a<0):
        fun2='y = '+str(c)
        fun2=fun2+' x^2 - '
        fun2=fun2+str(abs(a))
        fun2=fun2+' x'
        funtions.append(fun2)#Line equation   
      else:
        fun2='y = '+str(c)
        fun2=fun2+' x^2 + '
        fun2=fun2+str(a)
        fun2=fun2+' x +'
        fun2=fun2+str(b2)
        funtions.append(fun2)#Line equation    
        #fun2='y = '+str(m)
        #fun2=fun2+' x '
        #funtions.append(fun2)#Line equation
      interv2='For x in [ '+str(x[k])
      interv2=interv2+' ,'
      interv2=interv2+str(x[k+1])
      interv2=interv2+' ]'
      intervals.append(interv2)
      
    #last interval
    m3=(y[n-1]-y[n-2])/(x[n-1]-x[n-2]) #Find m with points k and k+1
    b3=y[n-2]-m*x[n-2] #Independent value
    if(b3>0):
        fun='y = '+str(m3)
        fun=fun+' x +'
        fun=fun+str(b3)
        funtions.append(fun)#Line equation
    elif(b3<0):
        fun='y = '+str(m3)
        fun=fun+' x -'
        fun=fun+str(abs(b3))
        funtions.append(fun)#Line equation
    else:
        fun='y = '+str(m3)
        fun=fun+' x '
        funtions.append(fun)#Line equation
    interv='For x in [ '+str(x[n-2])
    interv=interv+' ,'
    interv=interv+str(x[n-1])
    interv=interv+' ]'
    intervals.append(interv)
     
    
        
    matr=[funtions,intervals]
    print(len(funtions),len(intervals))
    return matr


