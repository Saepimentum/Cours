# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 18:12:57 2023

@author: 33783
"""

import math # pour utiliser le logarithme 


# =============================================================================

loga = -math.log(2) # print -log(2))

def S(a,n): #
    cpt = 0
    for k in range(1, n+1):
        cpt += (-1)**k/k**a
    return cpt

suite = (S(1,1000))

print('',loga,'\n',suite)

# =============================================================================

def Senca():
    n=1
    while S(1,2*n)-S(1,2*n+1) >= 0.001:
        n += 1
    print("l'encadrement de -ln(2) est: S( 1,",2*n,") <= -ln(2) <= S( 1,",2*n+1,")")
    return 2*n
