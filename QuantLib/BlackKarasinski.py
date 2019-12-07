# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 23:46:17 2017

@author: Xiao

Black-Karasinski Model
d ln(r_t) = [theta_t - a_t*ln(r_t)] dt + sigma_t dz

"""

#%% 
#import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np
import random
#%%
sigma = 0.1
a = 0.1
length = 25 # in years
timestep = np.int(360*length/6)
dt = length/timestep
sqrtDt = np.sqrt(dt)
theta = a*0.2
r0 = 0.01
#%%
def generate_paths(num_paths, timestep):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        lnr = np.log(r0)
        arr[i,0] = r0
        for j in range(1,timestep+1):
            vol = random.gauss(0, sigma)
            drift = theta - a*lnr
            lnr = lnr + drift * dt + vol * sqrtDt
            arr[i, j] = np.exp(lnr)
    time = np.arange(timestep+1)*dt
    return time, arr
#%%
num_paths = 10
time, paths = generate_paths(num_paths, timestep)
for i in range(num_paths):
    plt.plot(time, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Black-Karasinski Short Rate Simulation")
plt.show()
#%% validation
num_paths = 1000
time, paths = generate_paths(num_paths, timestep)
#%%
rateBK = [np.mean(paths[:, i]) for i in range(timestep+1)]
plt.plot(time, rateBK, "r-.", lw=3, alpha=0.6)
#plt.plot(time,np.exp(-a*time)*r0 + theta/a *(1-np.exp(-a*time)), "b-", lw=2, alpha=0.5)
plt.title("mean of Short Rates")
plt.show()
vol = [np.var(paths[:, i]) for i in range(timestep+1)]
plt.plot(time, vol, "r-.", lw=3, alpha=0.6)
#plt.plot(time,sigma*sigma/(2*a)*(1.0-np.exp(-2.0*a*np.array(time))), "b-", lw=2, alpha=0.5)
plt.title("Variance of Short Rates")
plt.show()

#%% compare with HW
plt.plot(time, rateHW, time, rateBK, lw=3, alpha=0.6)

