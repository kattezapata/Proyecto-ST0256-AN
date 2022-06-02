import numpy as np

#Simple gaussian elimination Method
#Input:(Matrix A, independent vector b)
def EGsimple(A,b):   
    n = len(A) #matriz A size or number of variables
    for i in range(n):
        A[i].append(b[i])
        
    #print(A)

    for k in range(n-1): #From 0 to n-2 - # columns
        for i in range(k+1,n):#From k+1 to n-1 - # rows
            mul=A[i][k]/A[k][k]
            A[i][k]=0
            for j in range(k+1,n+1):#From k+1 to n
                A[i][j]=A[i][j]-mul*A[k][j]
                
    x=substitution(A)
    return(x)

#Regressive substitution method 
#This method returns a vector of floats with the values of x. i.e. x=[x1_,x2_,x_3,x_4].  
#after the simple gaussian elimination of matrix A
#Input:(Matrix A that contains independent vector b)      
def substitution(A):
    n = len(A)
    X=[]
    for i in range(n):
        X.append(0)
    #print(X)
    for k in range(n-1,-1,-1):#va de n-1 hasta 0
        sum=0
        for j in range(k+1,n):#va de k+1 hasta n

            sum=A[k][j]*X[j]+sum
        #print(k)
        X[k]=(A[k][n]-sum)/A[k][k]
        #print(X[k])
            
    return(X)
            
#TESTING
M=[[3,6,-2,9],[-5,4,5,-6],[-3,8,2,-3],[-4,10,3,9]]
b=[6,5,3,9]
#matriz=[[3,2],[4,-3]]
#vector=[7,-2]
#print("Matrix A:",M)
#print("Independent vector: ",b)
#A=EGsimple(M,b)
#print("Result: ",A)
#print("X's value: ",substitution(A))

