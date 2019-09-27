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
import time
import statistics as st

def average_above_zero(tab):
    """Function that calculate average of array of positives int
    Args:
        array: an array
    Returns the moy
    """
    if not(isinstance(tab,list)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(tab)==0:
        raise ValueError('expected a non empty a list as input')
    if not(isinstance(tab[0],(int,float))):
        raise ValueError('average_above_zero, expected a list of numbers')
    #tab_zeros=np.zeros(12,dtype=np.int32)
    tab_fromList=np.array(tab)
    
    Som = 0
    N = 0
    for var in tab_fromList:
        if var>0:
            Som+=var
            N+=1
    Moy=Som/N
    return Moy

def max_value(tab):
    """Function that calculate max of array of int
    Args:
        array: an array
    Returns the max
    """
    tab_fromList=np.array(tab)
    max_var_index=0
    for i,var in enumerate(tab_fromList):
        if var>tab_fromList[max_var_index]:
            max_var_index=i
    return tab_fromList[max_var_index],max_var_index

def reverse_table(tab):
    """Function that reverse an array
    Args:
        tab: an array
    return the array reversed
    """
    tab_fromList=np.array(tab)
    #swap_var = 0
    for i,var in enumerate(tab_fromList):
        tab_fromList[i], tab_fromList[(i*-1)-1] = tab_fromList[(i*-1)-1], tab_fromList[i]
        print(tab_fromList[i])
        print(tab_fromList[(i*-1)-1])
    print(tab_fromList)
    return tab_fromList



        


#tab_list=np.random.randint(0,100000,1000).tolist()#Random array of 1000 positives int
tab_list=[10,15,24,16,85]
average = average_above_zero(tab_list)
print("moy =",average)
print("max = ",max_value(tab_list))
print("reverse =",reverse_table(tab_list))