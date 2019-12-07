from numpy import *
from math import *
from scipy.stats import norm
#%%
def black_scholes(type,s,k,r,T,v,q):
	print( str(s) + ", " +  str(k) + ", ")
	d1=(log(s/k)+(r-q+v**2/2)*T)/v/sqrt(T)
	d2=(log(s/k)+(r-q-v**2/2)*T)/v/sqrt(T)
	if (type=='c') or (type=='C'):
		return s*exp(-q*T)*norm.cdf(d1)-k*exp(-r*T)*norm.cdf(d2)
	elif (type=='p') or (type=='P'):
		return k*exp(-r*T)*norm.cdf(-d2) - s*exp(-q*T)*norm.cdf(-d1)
#%%	
def trisolve(amm,bbb):
	dim=int(sqrt(size(amm)))
	x=array([0.0] * dim)
	for i in range(1,dim):
		amm[i,i]=amm[i,i]-amm[i,i-1]/amm[i-1,i-1]*amm[i-1,i]
		bbb[i]=bbb[i]-amm[i,i-1]/amm[i-1,i-1]*bbb[i-1]
		amm[i,i-1]=0
	x[dim-1]=bbb[dim-1]/amm[dim-1,dim-1]
	for i in range(1,dim):
		ii=dim-1-i
		x[ii]=(bbb[ii]-amm[ii,ii+1]*x[ii+1])/amm[ii,ii]
	return x
	
#%%		
M=60; #strike dimension
N=20; #time steps
#T=1;
#r
#q
v=sigma;
#k
k=K;
dt=T/N;
AA=array([[0.0] * (N+1) for i in range(M+1)])
amatrix=array([[0.0] * (M+1) for i in range(M+1)])
A=array([0.0] * (M+1))
B=zeros_like(A)
C=zeros_like(A)

for i in range(1,M):
	A[i]=0.5*r*(i+1)*dt-0.5*v*v*(i+1)*(i+1)*dt
	B[i]=1+v*v*(i+1)*(i+1)*dt+r*dt
	C[i]=-0.5*r*(i+1)*dt-0.5*v*v*(i+1)*(i+1)*dt

for i in range(1,M):
	amatrix[i,i-1]=A[i]
	amatrix[i,i]=B[i]
	amatrix[i,i+1]=C[i]

for j in range(0,N):
	AA[0,j]=exp(-r*(N-j)*dt)*k
	AA[M,j]=black_scholes('p',M,k,r,(N-j)*dt,v,q)

for i in range(0,M+1):
	AA[i,N]=max(k-i,0)

for i in range(0,N): 
	I=N-i
	bcolumn=copy(AA[1:M,I])
	bcolumn[0]=bcolumn[0]-A[1]*AA[0,I-1]
	bcolumn[M-2]=bcolumn[M-2]-C[M-1]*AA[M,I-1]
	amm=copy(amatrix[1:M,1:M])
	AA[1:M,I-1]=trisolve(amm,bcolumn)

from matplotlib import cm	
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = arange(0, (N+1)*dt, dt)
Y = arange(0, M+1, 1)
X, Y = meshgrid(X, Y)
surf = ax.plot_surface(X, Y, AA, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.show()


