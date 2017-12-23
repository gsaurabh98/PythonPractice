# prime number less than 100
# 1,2,3,5,7,11,13,17,19 ....100

num = int(input('Enter the number:'))

def prime(self):
    for i in range(2, num):
        if (num % i) == 0:
            print '{0} is not prime numner'.format(num)
            print i, 'times', num // i, "is", num
            break
    else:
        print '{0} is prime numner'.format(num)

if num>1 and num>0:
	prime(num)
elif num<-1:
	prime(num)
else:
    print '{0} is prime numner'.format(num)