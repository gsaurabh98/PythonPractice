'''
Every module has a name and statements in a module can find out the name of its module.
This is especially handy in one particular situation - As mentioned previously,
when a module is imported for the first time, the main block in that module is run.
What if we want to run the block only if the program was used by itself and not when
it was imported from another module? This can be achieved using the __name__ attribute of the module.
'''

#!/usr/bin/python
# Filename: using_name.py

#below print will get executed along with else part if we import this module
print 'Hello World'

if __name__ == '__main__':
	print 'This program is being run by itself'
else:
	print 'I am being imported from another module'
