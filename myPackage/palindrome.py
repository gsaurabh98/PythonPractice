num = int(input('Enter a number:'))

temp = num
x =0
while temp>0:
    rem = temp%10
    x = rem + x*10
    temp = temp//10

if x == num:
    print num, 'is palindrome'
else:
    print num, 'is not palindrome'

# rem = 1, 2, 1     7,8
# temp = 12,1,0     8,0
