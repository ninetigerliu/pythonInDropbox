# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 23:46:17 2017

@author: Xiao
Hull - White Model
d r_t = [theta_t - a_t * r_t] dt + sigma_t dz

"""

#%% 
#import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import optimize
#%%
#%%
sigma = 0.01
a = 0.1
length = 25 # in years
timestep = np.int(360*length/6)
dt = length/timestep
sqrtDt = np.sqrt(dt)
theta = a*0.2
r0 = 0.01
#%%
time = np.arange(timestep+1)*dt
def generate_paths(num_paths, timestep, theta_x):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        r = r0
        arr[i,0] = r
        for j in range(1,timestep+1):
            vol = random.gauss(0, sigma)
            drift = theta_x - a*r
            r = r + drift * dt + vol * sqrtDt
            arr[i, j] = r
    return arr
#%%
num_paths = 10
paths = generate_paths(num_paths, timestep, theta)
for i in range(num_paths):
    plt.plot(time, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()
#%% validation
num_paths = 1000
paths = generate_paths(num_paths, timestep, theta)
#%%
rateHW = [np.mean(paths[:, i]) for i in range(timestep+1)]
plt.plot(time, rateHW, "r-.", lw=3, alpha=0.6)
plt.plot(time,np.exp(-a*time)*r0 + theta/a *(1-np.exp(-a*time)), "b-", lw=2, alpha=0.5)
plt.title("mean of Short Rates")
plt.show()
vol = [np.var(paths[:, i]) for i in range(timestep+1)]
plt.plot(time, vol, "r-.", lw=3, alpha=0.6)
plt.plot(time,sigma*sigma/(2*a)*(1.0-np.exp(-2.0*a*np.array(time))), "b-", lw=2, alpha=0.5)
plt.title("Variance of Short Rates")
plt.show()

#%% solver:
targetDF = 0.9
targetLength = 60*5
num_paths = 1000
def discountFactor( theta_x ):
    paths = generate_paths(num_paths, targetLength, theta_x)
    rateAverage = [np.mean(paths[:, i]) for i in range(targetLength)]
    rateAverage = np.array(rateAverage )
    df = np.exp(-sum(rateAverage*dt)) - targetDF
    print(df, theta_x)
    return df

theta0 = a*0.2
#theta0 = a
thetaSolution = optimize.newton(discountFactor, theta0, None, (), 1.e-02, 50)
print( thetaSolution )
#%%
paths = generate_paths(num_paths, targetLength, thetaSolution)
rateAverage = [np.mean(paths[:, i]) for i in range(targetLength)]
plt.plot(np.arange(targetLength)*dt, rateAverage, "r-.", lw=3, alpha=0.6)
np.var(paths[:, targetLength])

