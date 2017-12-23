num = range(1,20)
for i in num:
    if True:
        for x in range(2,i):
            if (i%x) ==0:
                break
        else:
            print i

