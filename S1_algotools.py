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
import cv2

#DISPLAY_TIME=False

def average_above_zero(tab):
    """Function that calculate average of array of positives int
    Args:
        array: an array
    Returns the moy
    """
    if not(isinstance(tab,list)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(tab)==0:
        raise ValueError('average_above_zero, expected a non empty a list as input')
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

def max_value(tab):#To test more
    """Function that calculate max of array of int
    Args:
        array: an array
    Returns the max
    """
    if not(isinstance(tab,list)):
        raise ValueError('max_value, expected a list as input')
    if len(tab)==0:
        raise ValueError('max_value, expected a non empty a list as input')
    if not(isinstance(tab[0],(int,float))):
        raise ValueError('max_value, expected a list of numbers')

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
    if not(isinstance(tab,list)):
        raise ValueError('max_value, expected a list as input')
    if len(tab)==0:
        raise ValueError('max_value, expected a non empty a list as input')
    if not(isinstance(tab[0],(int,float))):
        raise ValueError('max_value, average_above_zero, expected a list of numbers')

    tab_fromList=np.array(tab)
    size = int(len(tab_fromList)/2)
    for i in range(size):
        tab_fromList[i], tab_fromList[(i*-1)-1] = tab_fromList[(i*-1)-1], tab_fromList[i]
    return tab_fromList

def roi_bbox(input_image):
    """Function that find the bounding box of an array of 1 inside a 2D array
    Args:
        input_image: a 2D array
    return a 4x2 array with the four 2D coordinates (top-left,top,right,bottom-left,bottom-right)
    """
    if not(isinstance(input_image,np.ndarray)):
        raise ValueError('max_value, expected a np.ndarray as input')
    if len(input_image)==0:
        raise ValueError('max_value, expected a non empty np.ndarray as input')

    rows=len(input_image)
    cols=len(input_image[0])
    minR=-1
    maxR=-1
    minC=cols
    maxC=-1
    for r in range(rows):
        for c in range(cols):
            if(input_image[r][c]!=0):
                maxR=r
                if(minR==-1):
                    minR=r
                if(c<minC):
                    minC=c
                if(c>maxC):
                    maxC=c
    coords=[[minR,minC],[minR,maxC],[maxR,minC],[maxR,maxC]]
    return coords 

def random_fill_sparse(table, K):
    """Function that put K 'X' in an array
    Args:
        table: a 2D array
        K: the number of 'X' to put in the array
    return the table with 'X' in it
    """
    for i in range(K):
        hCoord=np.random.randint(len(table))
        wCoord=np.random.randint(len(table[0]))
        table[hCoord][wCoord]="X"
    return table

#tab_list=np.random.randint(0,1000000,1000).tolist()#Random array of 1000 positives int
'''tab_list=[10,15,24,95,16,85,35,58,63,14]

print("list : ",tab_list)
start_time = time.perf_counter()
average=average_above_zero(tab_list)
average_above_zero_time=(time.perf_counter()-start_time)*1000000 #to micro second
print("moy =",average)

start_time = time.perf_counter()
st.mean(tab_list)
mean_time=(time.perf_counter() - start_time)*1000000

start_time = time.perf_counter()
maxVal = max_value(tab_list)
max_value_time=(time.perf_counter() - start_time)*1000000
print("max = ",maxVal)

start_time = time.perf_counter()
max(tab_list)
max_time=(time.perf_counter() - start_time)*1000000

start_time = time.perf_counter()
reverse = reverse_table(tab_list)
reverse_table_time=(time.perf_counter() - start_time)*1000000
print("reverse =",reverse)

start_time = time.perf_counter()
reverse = tab_list.reverse()
reverse_time=(time.perf_counter() - start_time)*1000000

"""
matrix=np.zeros((10,10),dtype=np.int32)
matrix[3:6,4:8]=np.ones((3,4),dtype=np.int32)
print(matrix)
print(roi_bbox(matrix))
"""

img=cv2.imread("img_sample.png",0)
roi = roi_bbox(img)
print('roi_bbox : ',roi)
#cv2.rectangle(img, (roi[0][0],roi[0][1]), (roi[3][0], roi[3][1]), (255,255,255), 10)
#cv2.imshow("read img",img)
#cv2.waitKey()
charar=np.chararray((3, 3))
charar[:] = '0'
print(random_fill_sparse(charar,5))'''


'''
if(DISPLAY_TIME):
    print("\nTime : ")
    print("\naverage_above_zero() : ",average_above_zero_time,"microsecondes")
    print("mean() : ",mean_time,"microsecondes")
    print("mean() : ",round(average_above_zero_time/max_time,2),"x faster")
    print("\nmax_value() : ",max_value_time,"microsecondes")
    print("max() : ",max_time,"microsecondes")
    print("max() is ",round(max_value_time/max_time,2),"x faster")
    print("\nreverse_table() : ",reverse_table_time,"microsecondes")
    print("reverse() : ",max_time,"microsecondes")
    print("reverse() is ",round(reverse_table_time/reverse_time,2),"x faster")'''
