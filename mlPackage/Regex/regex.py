import re

NameAge = " John is 25 and Elina is 20 Matt is 40 and Kiara is 22 "

#find all return the matches in list
ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*',NameAge)

dict = {}
x = 0

for eachname in names:
    dict[eachname] = ages[x]
    x = x+1
print dict