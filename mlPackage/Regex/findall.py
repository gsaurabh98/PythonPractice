import re

text = 'We need to inform him about the latest information'

#findall return the result in list
re_text = re.findall('inform',text)

for i in re_text:
        print i

# to print the matching letter and ending with at
str = 'Sat,mat,hat,cat'

words = re.findall('[Smhc]at',str)

for i in words:
    print i

# match series of range of characters
str = 'Sat,mat,hat,cat'

words = re.findall('[h-m]at',str)

for i in words:
    print i

# ^[h-m] everything apart from h to m
str = 'Sat,mat,hat,cat'

words = re.findall('[^h-m]at',str)

for i in words:
    print i
