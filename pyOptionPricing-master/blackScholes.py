import math
from scipy.stats import norm

# Abramowitz and Stegun 7.1.26 approximation
def erf(x):
    
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p  =  0.3275911

    t = 1.0/(1.0 + p*x)
    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*math.exp(-x*x)

    return y

# custom erf implementation
def fnor1(x): 
    
    y=0.5*(1+erf(x/math.sqrt(2)));
    
    return y

# math erf implementation
def fnor2(x):

    y=0.5*(1+math.erf(x/math.sqrt(2)));
    
    return y
#%%
def myNormal( z ):
   y = 1.0 / (1.0 + math.fabs(z) * 0.2316419);
   x = ((((1.330274429  * y - 1.821255978) * y +
          1.781477937) * y - 0.356563782) * y +
        0.31938153)  * y;
   area = (0.398942280401433 * math.exp( z*z / -2.0) * x);

   if z >= 0.0:
      area = 1.0 - area;

   return area;  

#%%
def BS(t,St,K,T,r,q,sig,PorC):

    Tmt=T-t;
    ATmt=sig*math.sqrt(Tmt);
    logo=math.log(St/K);
    Ap=(logo+(r-q+0.5*sig**2)*Tmt)/ATmt;
    An=Ap-ATmt;
    print("Ap="+str(Ap))
    print("An="+str(An))
    print("fnor2(Ap)="+str(myNormal(Ap)))
    print("fnor2(An)="+str(myNormal(An)))
    
    if PorC == 'c':
        p=math.exp(-q*Tmt)*St*myNormal(Ap)-K*math.exp(-r*Tmt)*myNormal(An);
    elif PorC == 'p':
        p=K*math.exp(-r*Tmt)*myNormal(-An)-math.exp(-q*Tmt)*St*myNormal(-Ap);
    
    return p
#%%
def BS1(t,St,K,T,r,q,sig,PorC):

    Tmt=T-t;
    ATmt=sig*math.sqrt(Tmt);
    logo=math.log(St/K);
    Ap=(logo+(r-q+0.5*sig**2)*Tmt)/ATmt;
    An=Ap-ATmt;
    
    if PorC == 'c':
        p=math.exp(-q*Tmt)*St*norm.cdf(Ap)-K*math.exp(-r*Tmt)*norm.cdf(An);
    elif PorC == 'p':
        p=K*math.exp(-r*Tmt)*norm.cdf(-An)-math.exp(-q*Tmt)*St*norm.cdf(-Ap);
    
    return p
