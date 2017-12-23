import math

num = int(input('Enter the number:'))

#print 'factorial {0} is:'.format(num), math.factorial(num)

# 5 = 5*4*3*2*1

fact =1

if num<0:
    print 'Sorry, factorial does not exist for negative numbers'
elif (num==0):
    print 'Factorial of 0 is 1'
else:
    for i in range(1,num+1):
        fact = fact*i
    print 'Factorial of {0} is'.format(num), fact
