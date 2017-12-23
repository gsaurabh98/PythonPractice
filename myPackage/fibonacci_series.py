terms = int(input('Enter the terms:'))

n1 =0
n2 =1
count = 2

if terms <=0:
    print 'please enter positive terms '
elif terms ==1:
    print n1
else:
    print n1
    print n2
    while count < terms:
        n3 = n1+n2
        print n3
        n1 =n2
        n2 = n3
        count +=1





