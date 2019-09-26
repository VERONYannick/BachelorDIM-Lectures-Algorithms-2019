# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:04 2019

@author: verony
"""
'''
What happens if Som initialization is forgotten ?
    =>UnboundLocalError: local variable 'Som' referenced before assignment
    
What can you expect if all the values are below zero ?
    =>ZeroDivisionError: division by zero
'''
import numpy as np

def average_above_zero(arr):
    """Function that calculate average of array of positives int
    Args:
        array: an array
    Returns the moy
    """
    #tab_zeros=np.zeros(12,dtype=np.int32)
    tab_fromList=np.array(arr)
    
    Som = 0
    N = 0
    for var in tab_fromList:
        if var>0:
            Som+=var
            N+=1
    Moy=Som/N
    return Moy

tab_list=np.random.randint(0,100000,1000)#Random array of 1000 positives int
#tab_list=[10,15,24,16,85]
print("moy =",average_above_zero(tab_list))