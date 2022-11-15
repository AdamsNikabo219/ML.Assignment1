#!/usr/bin/env python
# coding: utf-8

# problem 1

# In[3]:


import numpy as np
x_ndarray=np.arange(-50,50.1,0.1)
y_ndarray=0.5*x_ndarray+1
x_ndarray,y_ndarray


# problem 2

# In[5]:


xy_ndarray=np.stack((x_ndarray,y_ndarray),-1)
print (xy_ndarray)
xy_ndarray.shape


# problem 3

# In[9]:


dx=np.diff(x_ndarray)
dy=np.diff(y_ndarray)
slope=dy/dx
slope=slope.reshape(slope.shape[0],1)
slope.shape


# problem 4

# In[14]:


import matplotlib.pyplot as plt
plt.xlabel ("X")
plt.ylabel("gradient")
plt.title("LINEAR FUNCTION")
plt.plot(x_ndarray,y_ndarray,color ='yellow', linewidth=3)
plt.show


# problem 5

# In[12]:


import numpy as np
def compute_gradient(function,x_range=(-50,50.1,0.1)):
    x_array=np.arange(*x_range)
    y_array=function(x_array)
    xy_array=np.concatenate((x_array[:,np.newaxis],y_array[:,np.newaxis]),axis=1)
    gradient=(xy_array[1:,1]-xy_array[:-1,1])/(xy_array[1:,0]-xy_array[:-1,0])
    return xy_array,gradient
def function1 (x_array):
    y_array=x_array**2
    return y_array
xy_array1,gradient1=compute_gradient(function1)
print(compute_gradient(function1))



# In[14]:


import matplotlib.pyplot as plt
plt.xlabel ("X")
plt.ylabel("Y")
plt.title("y=x**2")
plt.plot(xy_array1[:,0],xy_array1[:,1],color='green',linewidth=4)
plt.show()

plt.xlabel ("X")
plt.ylabel("gradient")
plt.title("GRADIENT OF Y=X**2")
plt.plot(xy_array1[:-1,0],gradient1,color='blue',linewidth=5)
plt.show()


# problem 6

# In[35]:


import numpy as np
def compute_gradient(function,x_range=(-50,50.1,0.1)):
    array_x=np.arange(*x_range)
    array_y=function(array_x)
    min_y_value=np.min(array_y)
    min_y_arg=np.argmin(array_y)
    array_xy=np.stack((array_x,array_y),-1)
    gradient=np.diff(array_y)/np.diff(array_x)
    return f'The minimum value of y for the functionis{min_y_value}and its index is{min_y_arg}'
         


# In[31]:


compute_gradient(function1)


# In[39]:


compute_gradient(function1,x_range=(-50,50.1,0.1))


# In[ ]:




