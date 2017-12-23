import re

str = '''
my name is saurabh
lives in bangalore
work in accenture.
'''

print str

text = re.compile('\n')

new_text = text.sub(' ',str)

print new_text

#\b: backslash
#\f: formfeed
#\r: carriage return
#\t: tab
#\v: vertical tab