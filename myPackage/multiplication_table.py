
x = int(input('Enter the number of your choice:'))

print 'Below is the table of {0}'.format(x)

for i in range(1,((x*10)/x)+1):
    print '{0}x{1}='.format(x,i), x*i