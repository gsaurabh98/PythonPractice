x = [(1,2),(3,4),(5,6)]

# below is the method for tuple unpacking, means we are print only values present in tuple

for (a,b) in x:
    print 'tuple first values is:', a
    print 'tuple second values is:', b

# (a,b) brackets are optional, we can use a,b
for a,b in x:
    print 'tuple first values is:', a
    print 'tuple second values is:', b