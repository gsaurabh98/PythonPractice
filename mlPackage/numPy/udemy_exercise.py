#Import NumPy as np
import numpy as np
import random

#Create an array of 10 zeros
print np.zeros(10)

#Create an array of 10 ones
print np.ones(10)

#Create an array of 10 fives
print (np.ones(10))*5

#Create an array of the integers from 10 to 50
print np.arange(10,51)

#Create an array of all the even integers from 10 to 50
print np.arange(10,51,2)

#Create a 3x3 matrix with values ranging from 0 to 8
print np.arange(9).reshape(3,3)

#Create a 3x3 identity matrix
print np.eye(3)

# Use NumPy to generate a random number between 0 and 1
print np.random.rand(1)

#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print np.random.randn(25)

#linearly spaced matrix from 0,1,100
print np.linspace(0.01,1,100).reshape(10,10)

#Create an array of 20 linearly spaced points between 0 and 1:
print np.linspace(0,1,20)

#Numpy Indexing and Selection
mat = np.arange(1,26).reshape(5,5)
print mat
print mat[2:,1:]
print mat[3,4]
print mat[0:3,1:2]
print mat[4,:]
print mat[3:5,:]

#Get the standard deviation of the values in mat
print np.sum(mat)

#Get the standard deviation of the values in mat
print np.std(mat)

#Get the sum of all the columns in mat
# var = np.array([sum(mat[0:5,0:1]) , sum(mat[0:5,1:2]) ,  sum(mat[0:5,2:3]) ,  sum(mat[0:5,3:4]) , sum(mat[0:5,4:5])])
# print var

print np.sum(mat,axis=0)
#or
print mat.sum(axis=0)