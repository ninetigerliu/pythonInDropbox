# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 21:13:21 2018

@author: Xiao Liu
"""

import numpy as np
import matplotlib.pyplot as plt


def A(vol, asset_step, risk_free_rate, dividend_rate, time_step):
    return 0.5*time_step*(vol**2*asset_step**2 - (risk_free_rate - dividend_rate)*asset_step)

def B(vol, asset_step, risk_free_rate, time_step):
    return 1 - time_step*(vol**2*asset_step**2 + risk_free_rate)

def C(vol, asset_step, risk_free_rate, dividend_rate, time_step):
    return 0.5*time_step*(vol**2*asset_step**2 + (risk_free_rate - dividend_rate)*asset_step)

def call_payoff(asset_price, strike_price):
    return max(asset_price - strike_price, 0)

S_max          = 140*2.
strike         = 100.
expiry         = 2.
asset_step     = 0.5
risk_free_rate = 0.05
dividend_rate  = 0.0
vol            = 0.2
t_step         = 0.00025/4

no_asset_steps = int(S_max/asset_step)
print "Number of asset steps: ", no_asset_steps

no_time_steps = int(expiry/t_step)
print "Number of time steps: ", no_time_steps

S = np.zeros(no_asset_steps+1)
V = np.zeros((no_asset_steps+1, no_time_steps+1))

for i in xrange(no_asset_steps+1):
    S[i] = i*asset_step
    V[i,no_time_steps] = call_payoff(S[i], strike)

for k in range(no_time_steps, 0, -1):
    for i in xrange(1,no_asset_steps):
        A_co = A(vol, i, risk_free_rate, dividend_rate, t_step)
        B_co = B(vol, i, risk_free_rate, t_step)
        C_co = C(vol, i, risk_free_rate, dividend_rate, t_step)
        V[i, k-1] = A_co*V[i-1, k] + B_co*V[i,k] + C_co*V[i+1,k]

    V[0, k-1] = 0
    V[no_asset_steps, k-1] = 2*V[no_asset_steps-1, k-1] - V[no_asset_steps-2, k-1]