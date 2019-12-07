
import numpy as np

gmean,gsigma,pathn = 0.0,0.001,100000
t,freq = 1,2
gsigma = gsigma*1/freq
initialCpn,alpha = 2.0,1.0

"""
cpnn = t*freq
gauss = np.random.normal(gmean,gsigma,(pathn,cpnn))
p = np.exp(gauss)
ppcum = np.cumprod(p,axis=1)
ppsum = ppcum.sum(axis=1)
print('real calculation: {0}'.format(np.std(ppsum)))
p0vector = [p[i][0] for i in range(pathn)]
"""


def approximate(initialCpn,t,freq,alpha,gsigma):
    cpnn = t*freq
    return initialCpn/freq*alpha/12*(cpnn**2-1)*gsigma

def simulation(gmean,gsigma,pathn,t,freq,initialCpn,alpha):
    cpnn = t*freq
    gauss = np.random.normal(gmean,gsigma,(pathn,cpnn))
    p = np.exp(gauss)
    ppcum = np.cumprod(p,axis=1)
    ppsum = ppcum.sum(axis=1)
    print('real calculation: {0}'.format(np.std(ppsum)))
    p0vector = [p[i][0] for i in range(pathn)]
    print(len(p0vector))
    print('approximate: {0}'.format(np.std([(1-np.power(p0,cpnn))/(1.0-p0)*p0 for p0 in p0vector])))
    tp = []
    for p0 in p0vector:
        tp.append(sum(np.power(p0,i+1) for i in range(cpnn)))
    print('approximate1:{0}'.format(np.std(tp)))

    cpnPayment = np.array([initialCpn/freq*(alpha*i+1) for i in range(cpnn)])
    ppsumWithCpn = np.matmul(ppcum,np.transpose(cpnPayment))
    averageCpn = np.array([ppsumWithCpn[i]/ppsum[i] for i in range(pathn)])
    return np.std(averageCpn)

def test(initialCpn,t,freq,alpha,pathn):
    cpnn = t*freq
    initialCpn /= freq
    gauss = np.random.normal(gmean,gsigma,pathn)
    p = np.exp(gauss)
    return np.std([initialCpn+initialCpn*alpha*p0/(1-np.power(p0,cpnn))*(1.0+(1-np.power(p0,cpnn-2))*p0/(1-p0)-np.power(p0,cpnn-1)*(cpnn-1)) for p0 in p])
