# import complex math module  
import cmath

a = input('Enter the value of a:')
b = input('Enter the value of b:')
c = input('Enter the value of c:')

x = (-b + cmath.sqrt(b**2 - 4*a*c))/2*a
y = (-b - cmath.sqrt(b**2 - 4*a*c))/2*a

print '{0} {1}'.format(x,y)
