import re
str = 'We need to inform him about the latest information'

text= re.finditer('inform',str)

# span pulls the starting and ending postion
for i in text:
    re_tuple = i.span()
    print re_tuple