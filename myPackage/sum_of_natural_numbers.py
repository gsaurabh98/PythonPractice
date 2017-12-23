num = int(input('Enter the Number:'))
sum =0
if num<0:
    print 'Please enter the postive number'
else:
    while num>0:
        sum +=num
        num -=1
    print sum