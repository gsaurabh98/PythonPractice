
# given input is an armstrong number

# num = int(input('Enter the Number:'))
# temp = num
# sum =0
# while temp>0:
#     n1 = temp%10
#     temp //=10
#     sum += n1**3
# if sum == num:
#     print num, 'is an Armstrong number'
# else:
#     print num, 'is not an Armstrong number'

#armstrong number between range

lower = int(input('Enter the lower digit:'))
upper = int(input('Enter the upper digit:'))
for num in range(lower,upper+1):
    temp = num
    sum =0
    while temp>0:
        n1 = temp%10
        temp = temp // 10
        sum += n1**3
        if num == sum:
            print num, 'is an Armstrong number'