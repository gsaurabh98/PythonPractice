
dict = {'x':1,'y':2,'z':3}
lst = [1,2,3,4,5,6]
tple = (1,2,3,4)

gen_expr = (x*x for x in range(3))

def my_func(x,y,z):
    print '< %d, %d, %d >' % (x,y,z)

def my_func2(x,y,z):
    print '< %s, %s, %s >' % (x,y,z)

my_func2(*dict)
my_func(**dict)
my_func(*lst[3:])
my_func(*tple[:3])
my_func(*gen_expr)