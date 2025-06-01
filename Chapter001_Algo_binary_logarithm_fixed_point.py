# -*- coding: utf-8 -*-
"""
Created on Mon May 26 17:06:32 2025

@author: sivad
"""

import numpy as np

#=================================================================
# README:
# Chapter001_Algo_binary_logarithm_fixed_point
# Ref: https://en.wikipedia.org/wiki/Binary_logarithm
# Iterative Approximation: 
# https://en.wikipedia.org/w/index.php?title=Binary_logarithm&action=edit&section=16
# Code to extract y= log2(x)
# Niter= No of times to iterate to extract the Fractional
#=================================================================

def float2fixed(x,PrecInpList):
    
    xF= np.floor(x*2**PrecInpList[1]).astype('int')
        
    return xF

    
#=================================================================
# Code Inputs
#=================================================================

x= 15.78614118751 # input for log2(x), can be any floating point number: Max number should be 127.XXXXX...

Niter= 12 # No of iterations for log2 fractional outer loop.

PrecInp= '7Q17' #Input x will be represented to this precision

PrecInpList= list(map(int,PrecInp.split('Q')))

PrecOut= '3Q21' #Output y=log2(x) will be represented to this precision

PrecOutList= list(map(int,PrecOut.split('Q')))

#=================================================================
# Fix Input Data Precision
#=================================================================

xF= float2fixed(x,PrecInpList) #'PrecInp= '7Q17' 

xFDecimal= xF/2**PrecInpList[1]

#=================================================================
# Integer calculation by shift right till nmber becomes 1
#=================================================================

y= xF>>PrecInpList[1] # Pick integer part, shift the Q.PrecInpList[1] to begin with.

N= 0
while (y>1):
    #print(N,y)
    y= y>>1
    N+= 1


#=================================================================
# Fractional Calculations
#=================================================================

#=================================================================
# Compute alpha as x/2^N
#=================================================================

alpha= xF>>N

PrecAlpha= '1Q23'
PrecAlphaList= list(map(int,PrecAlpha.split('Q')))

#=================================================================
# Change alpha representation - add more fractional bits
#=================================================================

alphq= alpha<<(PrecAlphaList[1]-PrecInpList[1])

#alphq= int(alphq)

#=================================================================
# Fractional 2 loops: Inner loop gets 1 valid fractiona location
#=================================================================

z= alphq
mvals= []

for k in range(Niter):
    count=0
    msb= z>>23
    while (msb==1):
        p= int(z)*int(z)
        z= p>>23
        msb= z>>23
        count+=1
        #print(count,z)
    
    print('Iteration No: ',k,count,z)
    z= z>>1
    mvals.append(count)
    
mvals=np.array(mvals)

F=0
mloc= np.cumsum(mvals)

print('\n========================= Run logs ========================================\n')
print('log2(x) and x='+str(x)+'\n')
print('x is represented as '+PrecInp, 'x used post fixed pointing is ',xFDecimal,'\n')
print('Integer part=N of log2('+str(x)+')=',N,'\n')
print('mvals index /fixed: ',mvals,'\n')
print('mvals cumsum/fixed: ',mloc,'\n')

for k in range(Niter):
    F+= 1/2**mloc[k]

logCalcu= N+F
lofTruth= np.log2(xF/2**PrecInpList[1])
error= logCalcu-lofTruth

print(f"Calculated log2( {xFDecimal:<20} = {logCalcu:20}")
print(f"True       log2( {x:<20} = {lofTruth:20}")
print(f"Error= {error:20}")

  
