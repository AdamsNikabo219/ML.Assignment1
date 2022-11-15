#!/usr/bin/env python
# coding: utf-8

# problem 1 manual multiplication of matrix
# 
# A= ([[-1,2,3],[4,-5,6],[7,8,-9]])
# B= ([[0,2,1],[0,2,-8],[2,9,-1]])
# Answering steps:
# step 1: multiplication of every matrix
# (-1*0)+(2*0)+(3*2) (-1*2)+(2*2)+(3*9) (-1*1)+(2*-8)+(3*-1) line 1
# (4*0)+(-5*0)+(6*2) (4*2)+(-5*2)+(6*9) (4*1)+(-5*-8)+(6*-1) line 2
# (7*0)+(8*0)+(-9*2) (7*2)+(8*2)+(-9*9) (7*1)+(8*-8)+(-9*-1) line 3
# step 2: The above result infomation
# ((0+0+6) (-2+4+27) (-1-16-3)) line 1
# ((4-0+12) (8-10+54) (4+40-6)) line 2
# ((0+0-18) (14+16-81) (7-64+9)) line 3
# [[6 29 -20]
# [12 52 38
# [-18 -51 -48]]
# 

# problem 2

# In[9]:


import numpy as np
a_ndarray=np.array([[-1,2,3],[4,-5,6],[7,8,-9]])
b_ndarray=np.array([[0,2,1],[0,2,-8],[2,9,-1]])
ab_ndarray=a_ndarray@b_ndarray
print(ab_ndarray)
     


# problem 3

# In[4]:


sum_of_ab_ndarray=(a_ndarray[1][0]*b_ndarray[0][1]+(a_ndarray[1][1]*b_ndarray[1][1]+(a_ndarray[1][2]*b_ndarray[2][1])))
print (sum_of_ab_ndarray)


# problem 4

# In[2]:


import numpy as np
a_ndarray=np.array([[-1,2,3],[4,-5,6],[7,8,9]])
b_ndarray=np.array([[0,2,1],[0,2,8],[2,9,-1]])
def product_of_matrix(a,b):
    ab_ndarray=np.empty([3,3])
    for row in range(a.shape[0]):
        for column in range(b.shape[1]):
            ab_ndarray[row][column]=sum(a[row,:]*b[:,column])
    return ab_ndarray
print (product_of_matrix(a_ndarray,b_ndarray))


# problem 5

# In[4]:


d_ndarray=np.array([[-1,2,3],[4,-5,6]])
e_ndarray=np.array([[-9,8,7],[6,-5,4]])
if (d_ndarray.shape[0]==e_ndarray.shape[1]):
    print (product_of_matrix(d_ndarray.e_ndarray))
else:
        print("there is a problem with the size of the matrix,which may result in incorrectcalculation")


# problem 6

# In[7]:


f_ndarray=d_ndarray.T
print(product_of_matrix(f_ndarray,e_ndarray)) 

