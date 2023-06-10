import numpy as np

W = np.array([
    [1, -3, 5], 
    [2, 4, -6]])
b = np.array([-1, 1, 2])
a_in = np.array([-2, 4])

def g(z):
    return 0 #sigmoid function should be here

def dense(a_in, W, b):
    units = W.shape[1]   # W.shape is a tuple with values (2, 3). So W.shape[1] is 3.  
    a_out = np.zeros(units)  # a_out is [0. 0. 0.]
    for j in range(units):    
        w = W[:,j]
        z = np.dot(w, a_in) + b[j]
        a_out[j] = g(z)  # assume g is defined outside of dense() and is the sigmoid function
    return a_out



