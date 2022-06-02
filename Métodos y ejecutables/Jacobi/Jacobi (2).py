import numpy as np
import pprint

def jacobi(a,b,x): 
	n=len(x) 
	t=x.copy()
	for  i  in  range(n): 
		s=0
		for j in range(n): 
			if i!=j:
				s=s+a[i,j]*t[j]
				x[i]=(b[i]-s)/a[i,i]
	return x


def jacobim(a,b,x,tol,Nmax): 
	n=len(x)  
	t=x.copy()
	for  k  in  range(Nmax): 
		x=jacobi(a,b,x)
		d=np.linalg.norm(np.array(x)-np.array(t),np.inf)
		print ("For iteration "+str(k+1)+": X = "+str(np.transpose(x.round(7)))+"\tError: "+str(abs(d)))
		if d<tol:
			return [x,k] 
		else:
			t=x.copy() 
	return [[],Nmax]

#xant=x;
#E=1000;

# Array to use
#A = np.array([[[10,-1,2,0],
# [-1,11,-1,3],
# [2,-1,10,-1],
# [0,3,-1,8]],float)

# Vector Solution
#b = np.array([[6],[25],[-11],[15]],float)

# Start Vector
#x=np.array([[0],[0],[0],[0]],float)

# Number of iterations
# Nmax=1000

#print ("array A:")
#pprint.pprint(A)
#print ("\nVector b:")
#pprint.pprint(b)

#print("")

# X is the solution and k the iterations
#[x,k]=jacobim(A,b,x,1.e-14,Nmax)

#if(k==Nmax):
# print("The method diverges or does not converge for the requested error bound.").

#else: 
# print("The vector 'x' is:")
# print(x)

# print("The number of iterations is: "+str(k+1))
