import numpy as np

var = np.arange(1,10)

#print var

var2 = np.array([1,3,25,'hello','x'])
# for i in var2:
#     print i

print 'type of array:', type(var2)
print 'dimension of array',var2.ndim
print 'shape of array', var2.shape
print 'size of array', var2.size
print 'datatype of array', var.dtype