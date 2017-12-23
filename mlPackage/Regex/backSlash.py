import re

str = 'what are you \\doing'

#one backslash will be ingnored ro overcome, we use below syntax
print (re.search(r'\\doing',str),str)