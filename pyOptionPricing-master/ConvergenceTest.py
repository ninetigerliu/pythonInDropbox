# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 13:54:40 2018

@author: Xiao Liu
"""
import math

#%% Black Schole 
#BS(t,St,K,T,r,sig,PorC):
    t=0.
    S=1200.
    K=1200.
    T=0.14
    sig=0.08
    r = 0.015


optionTypeCall='c'
pCall = BS(t,S,K,T,r,sig,optionTypeCall)
#pCall1 = BS1(t,S,K,T,r,sig,optionTypeCall)
optionTypePut = 'p'
pPut = BS(t,S,K,T,r,sig,optionTypePut)
print( "call price ="+str(pCall) )
#print( "call price 1  ="+str(pCall1) )
print( "put price ="+str(pPut) )

#%% CCR tree
#CRRTree(K,T,S,sig,r,N,PorC)
N = 100
pCallTree = CRRTree(K,T,S,sig,r,N,optionTypeCall)
print( "call price from crr= "+str(pCallTree) )

#%%
N0=100
for i in range (2, 100, 2):
    print( "i="+str(i) )
    N = N0*i
    pCallTree = CRRTree(K,T,S,sig,r, N ,optionTypeCall)
    print( "N="+ str(N) +"call price from crr= "+str(pCallTree) )
    print( "diff with BS = " + str(pCallTree-pCall) )
#%%
S0 = 1295.20
S = 1294.92909923709000
K = 1298.44330834882
#K = 1295
sigma = 0.088094592936283203
#sigma = 1e-8
T = 49./365.
r = 0.0159375107555
q = -0.0026636993840
#callPriceWithD = black_scholes('c',S,K,r,T,sig,q)
callPriceWithD_true = BS1(t,S,K,T,r,q,sigma,optionTypeCall)
print( callPriceWithD )
callPriceWithD = BS(t,S,K,T,r,q,sigma,optionTypeCall)
print( callPriceWithD )

N = 10000
pCallTree = CRRTree(K,T,S,sigma,r,q,N,optionTypeCall)
print( "call price from crr= "+str(pCallTree) )
print( "N="+str(N)+","+"error="+str(pCallTree-callPriceWithD_true))

N = 15000
pCallTree = CRRTree(K,T,S,sigma,r,q,N,optionTypeCall)
print( "call price from crr= "+str(pCallTree) )
print( "N="+str(N)+","+"error="+str(pCallTree-callPriceWithD_true))

N = 18000
pCallTree = CRRTree(K,T,S,sigma,r,q,N,optionTypeCall)
print( "call price from crr= "+str(pCallTree) )
print( "N="+str(N)+","+"error="+str(pCallTree-callPriceWithD_true))

#%%
N0=100
k=0
AA = []
NN = []
for i in range (0, 8):
    print( "i="+str(i) )
    N = N0*2**i
    pCallTree1 = CRRTree(K,T,S,sigma,r,q, N ,optionTypeCall)
    pCallTree2 = CRRTree(K,T,S,sigma,r,q, N ,optionTypeCall)
    pCallTree = (pCallTree1+pCallTree2)/2.0
    print( "N="+ str(N) +", call price from crr= "+str(pCallTree) )
    print( "diff with BS = " + str(pCallTree-callPriceWithD_true) )
    AA.append( pCallTree-callPriceWithD_true )
    NN.append( N )
    k=k+1
#%%
N = 20000
print( (CRRTree(K,T,S,sigma,r,q, N ,optionTypeCall) + CRRTree(K,T,S,sigma,r,q, N+1 ,optionTypeCall))/2. )