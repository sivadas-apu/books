# -*- coding: utf-8 -*-
"""
Created on Mon May 26 17:06:32 2025

@author: sivad
"""

import numpy as np

#=================================================================
# README:
# Chapter001_Algo_binary_logarithm_floating_point
# Ref: https://en.wikipedia.org/wiki/Binary_logarithm
# Iterative Approximation: 
# https://en.wikipedia.org/w/index.php?title=Binary_logarithm&action=edit&section=16
# Code to extract y= log2(x)
# Niter= No of times to iterate to extract the Fractional
#=================================================================

#=================================================================
# Code Inputs
#=================================================================

x= 100 # input for log2(x)

Niter= 12 # No of iterations for log2 fractional

#=================================================================
# Integer calculation by shift right till nmber becomes 1
#=================================================================

y= x
N= 0
while (y>1):
    print(N,y)
    y= y>>1
    N+= 1

print('Integer part of log2 of '+str(x)+'=',N)

#=================================================================
# Fractional Calculations
#=================================================================

#========================================
# Shift Right to create decimals
#========================================

Nf=15

alpha= x/2**N

alphaFrac= np.round((alpha-1)*2**Nf).astype('int')

#print(alpha,1+alphaFrac/2**Nf)

z= alpha
mvals= []

for k in range(Niter):
    count=0
    while (z<2):
        z= z*z
        count+=1
        #print(count,z)
    
    print('Iter: ',k,count,np.round(z,5))
    z= z/2
    mvals.append(count)
    
mvals=np.array(mvals)

print('mvals/floating: ',mvals)

F=0
mloc= np.cumsum(mvals)

for k in range(Niter):
    F+= 1/2**mloc[k]

logCalcu= N+F
lofTruth= np.log2(x)
error= logCalcu-lofTruth

print(logCalcu,lofTruth,error)    
